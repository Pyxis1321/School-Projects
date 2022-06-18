using System;
using Dragon_Hero.Items;
using System.Collections.Generic;
using System.Text;
using System.Diagnostics.CodeAnalysis;
using System.Collections;
using Dragon_Hero.Randomness;

namespace Dragon_Hero.Characters
{
    public abstract class Character : IComparable<Character>
    {
        public string Name { get; set; }
        public int Health { get; set; }
        public int MaxDmg { get; set; }
        public int MaxDef { get; set; }
        public int Weight { get; set; }

        public int maxHealth;

        protected ChanceGen generate = ChanceGen.Instance;

        public event Action<Character, Character> ChosenAnEponent;

        public Character(string Name, int Health, int MaxDamage, int MaxDefense, int Weight)
        {
            this.Name = Name;
            this.Health = Health;
            this.MaxDmg = MaxDamage;
            this.MaxDef = MaxDefense;
            this.Weight = Weight;
            maxHealth = Health;
        }

        public virtual void Attack(Character enemy)
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

            Console.WriteLine($"{Name} attacked for: {printDamage} - {MaxDmg}");
            Console.WriteLine($"{enemy.Name} is left with " + enemy.Health + " HP");
        }



        public virtual int Defense()
        {
            int defense = 0;
            if (generate.NextDouble() <= 0.5)
            {
                defense = generate.Next(0, MaxDef);
                Console.WriteLine($"{Name} defendses with: " + defense);
            }
            return defense;
        }

        public bool IsAlive()
        {
            if (Health > 0)
            {
                return true;
            }
            else
            {
                return false;
            }
        }

        public virtual int AddWeight()
        {
            return Weight;
        }

        public virtual Character ChoosingEnemy(List<Character> characters)
        {
            Character enemy = null;

            foreach (var character in characters)
            {
                if (this != character && character.IsAlive() && ControlChoosing(character))
                {
                    enemy = character;
                    ChosenAnEponent?.Invoke(this, enemy);
                    break;
                }
            }
            return enemy;
        }

        protected abstract bool ControlChoosing(Character character);

        public bool ChanceToFlee(Character character)
        {
            int health = this.Health;
            if (health < maxHealth * 0.1 && generate.NextDouble() <= 0.3)
            {
                ColorfullConsole.WriteLine($"{Name} fled the batlefield", ConsoleColor.Red);
                return true;
            }
            else return false;
        }

        public int CompareTo([AllowNull] Character other)
        {
            if (other == null)
                return 1;

            return this.CalcPower().CompareTo(other.CalcPower());

        }

        public override string ToString()
        {
            return $"Name: {Name}, Power: {CalcPower()}, Health: {maxHealth}, Damage: {MaxDmg}, Defense: {MaxDef}";
        }

        public virtual double CalcPower()
        {
            return (this.MaxDef + this.MaxDmg + this.MaxDef) / 3;
        }
    }
}
