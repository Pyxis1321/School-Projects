using System;
using Dragon_Hero.Items;
using System.Collections.Generic;
using System.Text;
using Dragon_Hero.Randomness;

namespace Dragon_Hero.Characters
{
    public class Hero : Character
    {
        protected ChanceGen generate = ChanceGen.Instance;

        public  Sword Sword { get; set; }
        public Shield Shield { get; set; }

        public Hero(string name, int health, int maxDamage, int maxDefense, int Weight, Sword sword = null, Shield shield = null) : base(name, health, maxDamage, maxDefense, Weight)
        {
            this.Sword = sword;
            this.Shield = shield;
        }

        public override void Attack(Character enemy)
        {
            if (Sword != null)
            {
                SwordAttack(enemy);
            }
            else
            {
                int dmg = Convert.ToInt32(generate.NextDouble() * MaxDmg);
                int defense = enemy.Defense();
                int printDamage = dmg;
                if (dmg > defense)
                {
                    dmg -= defense;
                    enemy.Health -= dmg;
                }
                else
                {
                    dmg = 0;
                }

                if (enemy.Health < 0)
                {
                    enemy.Health = 0;
                }

                Console.WriteLine($"{Name} attacked for: {printDamage}");
                Console.WriteLine($"{enemy.Name} is left with " + enemy.Health + " HP");
            }
        }

        public override int Defense()
        {
            if(Shield != null)
            {
                int shield = ShieldDefense();
                ColorfullConsole.Write($"{Name} defendses with: {shield}", ConsoleColor.Green);
                return shield;
            }
            else
            {
                int defense = 0;
                if (generate.NextDouble() <= 0.5)
                {
                    defense = generate.Next(0, MaxDef);
                    ColorfullConsole.Write($"{Name} defendses with: {defense}", ConsoleColor.Green);
                }
                    return defense;
            }
        }
        void SwordAttack(Character enemy)
        {
            int swordDamage = Sword.ItemDamage;
            int baseDamage = Convert.ToInt32(generate.NextDouble() * MaxDmg);
            baseDamage += swordDamage;
            int defense = enemy.Defense();
            int printDamage = baseDamage;
            if (baseDamage > defense)
            {
                baseDamage -= defense;
                enemy.Health -= baseDamage;
            }
            else
            {
                baseDamage = 0;
            }

            if (enemy.Health < 0)
            {
                enemy.Health = 0;
            }

            Console.WriteLine($"{Name} attacked for: {printDamage}");
            Console.WriteLine($"{enemy.Name} is left with " + enemy.Health + " HP");
        }
        int ShieldDefense()
        {
            {
                int shield = Shield.ItemDefense;
                int defense = 0;
                if (generate.NextDouble() <= 0.5)
                {
                    defense = generate.Next(0, MaxDef) + shield;
                }
                return defense;
            }
        }

        protected override bool ControlChoosing(Character enemy)
        {
            return enemy != this && enemy.IsAlive() && enemy.GetType() != this.GetType();
        }

        public override int AddWeight()
        {
            if(Sword != null)
            {
                Weight += Sword.ItemWeight;
            }
            else if(Shield!= null)
            {
                Weight += Shield.ItemWeight;
            }
            return Weight;
        }

        public override double CalcPower()
        {
            return (maxHealth + (MaxDmg + Sword?.ItemDamage ?? 0) + (MaxDef + Shield?.ItemDefense ?? 0)) / 3;
        }
    }
}
