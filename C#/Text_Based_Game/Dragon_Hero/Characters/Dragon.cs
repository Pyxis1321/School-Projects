using System;
using Dragon_Hero.Items;
using System.Collections.Generic;
using System.Text;
using Dragon_Hero.Randomness;

namespace Dragon_Hero.Characters
{
    public class Dragon : Character
    {
        public Claws Claws { get; set; }
        public Armor Armor { get; set; }

        public Dragon(string name, int health, int maxDamage, int maxDefense, int Weight, Claws claws = null, Armor armor = null) : base(name, health, maxDamage, maxDefense, Weight)
        {
            this.Claws = claws;
            this.Armor = armor;
        }

        protected ChanceGen generate = ChanceGen.Instance;

        public override void Attack(Character enemy)
        {
            int dmg2 = Claws.ItemDamage;
            int dmg = Convert.ToInt32(generate.NextDouble() * MaxDmg);
            dmg += dmg2;
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

        public override int Defense()
        {
            if (Armor != null)
            {
                int shield = ShieldDefense();
                ColorfullConsole.Write($"{Name} defendses with: {shield}", ConsoleColor.DarkMagenta);
                return shield;
            }
            else
            {
                int defense = 0;
                if (generate.NextDouble() <= 0.5)
                {
                    defense = generate.Next(0, MaxDef);
                    ColorfullConsole.Write($"{Name} defendses with: {defense}", ConsoleColor.DarkMagenta);
                }
                return defense;
            }
        }

        protected override bool ControlChoosing(Character enemy)
        {
            return enemy != this && enemy.IsAlive() && enemy.GetType() != this.GetType();
        }

        int ShieldDefense()
        {
            {
                int shield = Armor.ItemDefense;
                int defense = 0;
                if (generate.NextDouble() <= 0.5)
                {
                    defense = generate.Next(0, MaxDef) + shield;
                }
                return defense;
            }
        }

        public override double CalcPower()
        {
            return (maxHealth + (MaxDmg + Claws?.ItemDamage ?? 0) + (MaxDef + Armor?.ItemDefense ?? 0)) / 3;
        }
    }
}
