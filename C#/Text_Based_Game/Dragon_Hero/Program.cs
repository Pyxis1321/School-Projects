using Dragon_Hero.Characters;
using Dragon_Hero.Items;
using System;
using System.Collections.Generic;
using System.Linq;
using Dragon_Hero.Randomness;

namespace Dragon_Hero
{
    class Program
    {
        static void Main(string[] args)
        {
            Sword sw1 = new Sword("Wooden stick", 2, 0, 2);
            Sword sw2 = new Sword("Handmade wooden sword", 2, 0, 2);

            Shield sh1 = new Shield("Wooden door", 10, 5);

            Claws cw1 = new Claws("Crow Talons", 2, 0, 2);

            Hero hero = new Hero("Cthaat", 1000, 40, 40, 70, sw1, sh1);
            Hero hero2 = new Hero("Aylith", 1000, 80, 30, 85, sw2);

            Dragon dragon = new Dragon("Azathoth", 1000, 73, 30, 500, cw1);
            Dragon dragon2 = new Dragon("Ammutseba", 1000, 100, 10, 700, cw1);

            List<Character> characters = new List<Character>();
            characters.Add(dragon);
            characters.Add(hero);
            characters.Add(hero2);
            characters.Add(dragon2);

            characters.Sort();
            Console.WriteLine(String.Join(Environment.NewLine, characters));
            Console.WriteLine(Environment.NewLine + Environment.NewLine);

            for (int j = characters.Count - 1; j >= 0; j--)
            {
                Console.WriteLine(characters[j]);
            }
            Console.WriteLine(Environment.NewLine + Environment.NewLine);

            double averagePow = characters.Average(character => character.CalcPower());
            ColorfullConsole.WriteLine($"Average power of characters is: {averagePow}", ConsoleColor.Yellow);

            double minPow = characters.Min(c => c.CalcPower());
            Character weakestCharacter = characters.Find(c => c.CalcPower() == minPow);
            ColorfullConsole.WriteLine($"Weakest character is {weakestCharacter}", ConsoleColor.Yellow);

            double maxPow = characters.Max(c => c.CalcPower());
            Character strongestCharacter = characters.Find(c => c.CalcPower() == maxPow);
            ColorfullConsole.WriteLine($"Strongest character is {strongestCharacter}", ConsoleColor.Yellow);

            ColorfullConsole.WriteLine("Characters with power above the average:", ConsoleColor.Yellow);
            List<Character> strongerThenAverage = characters.FindAll(c => c.CalcPower() > averagePow);
            ColorfullConsole.WriteLine(String.Join(Environment.NewLine, strongerThenAverage), ConsoleColor.Yellow);

            ColorfullConsole.WriteLine("Characters with power below the average:", ConsoleColor.Yellow);
            List<Character> weakerThanAverage = characters.FindAll(c => c.CalcPower() < averagePow);
            ColorfullConsole.WriteLine(String.Join(Environment.NewLine, weakerThanAverage), ConsoleColor.Yellow);

            ColorfullConsole.WriteLine("Dragons on the batlefield are:", ConsoleColor.Yellow);
            List<Character> dragons = characters.FindAll(c => c is Dragon);
            ColorfullConsole.WriteLine(String.Join(Environment.NewLine, dragons), ConsoleColor.Yellow);

            double averageStrenght = characters.Average(c => c.MaxDmg);

            double averageDefense = characters.Average(c => c.MaxDef);
            averageDefense /= 4;
            int amountOfAbove = characters.Count(c => c.MaxDef > averageDefense);

            characters.ForEach(c => c.ChosenAnEponent += ChoosenOpenent);
            
            if(amountOfAbove == characters.Count)
            {
                ColorfullConsole.WriteLine("All characters have defense abowe one quarter of average", ConsoleColor.Yellow);
            }
            else if(amountOfAbove <= characters.Count)
            {
                ColorfullConsole.WriteLine("Some characters have defense below the average", ConsoleColor.Yellow);
            }

            Console.WriteLine(Environment.NewLine + Environment.NewLine);

            bool flee = true;

            for(int z = 0; z < characters.Count; z++)
            {
                Character rWeight = characters[z];
                rWeight.AddWeight();
            }

            for (int i = 0; HerosAlive(characters) > 0 && DragonsAlive(characters) > 0; i++)
            {
                Console.WriteLine($"Round {i + 1}:");
                for (int j = 0; j < characters.Count; ++j)
                {
                    Character attacker = characters[j];
                    if (attacker.IsAlive())
                    {
                        Character enemy = attacker.ChoosingEnemy(characters);
                        if (enemy != null)
                        {
                            flee = enemy.ChanceToFlee(enemy);
                        }
                        if (enemy != null && flee == false)
                        {
                            attacker.Attack(enemy);
                            if (enemy.Health <= 0)
                            {
                                characters.Remove(enemy);
                            }
                        }
                        else if (enemy != null && flee == true)
                        {
                            characters.Remove(enemy);
                        }
                            else continue;

                        Console.WriteLine(Environment.NewLine + Environment.NewLine);
                    }
                }
            }

            if (HerosAlive(characters) > 0)
            {
                Console.WriteLine("Heros won");
            }
            else if (DragonsAlive(characters) > 0)
            {
                Console.WriteLine("Dragon won");
            }

            ColorfullConsole.WriteLine("Left alive and with damage abouve average", ConsoleColor.Yellow);
            List<Character> remainingAboveAverage = characters.FindAll(c => c.MaxDmg > averageStrenght);
            ColorfullConsole.WriteLine(String.Join(Environment.NewLine, remainingAboveAverage), ConsoleColor.Yellow);

        }
        public static int HerosAlive(List<Character> characters)
        {
            int heroesAlive = 0;
            foreach (Character character in characters)
            {
                if (character is Hero && character.IsAlive())
                {
                    ++heroesAlive;
                }
            }
            return heroesAlive;
        }

        public static int DragonsAlive(List<Character> characters)
        {
            int dragonsAlive = 0;
            foreach (Character character in characters)
            {
                if (character is Dragon && character.IsAlive())
                {
                    ++dragonsAlive;
                }
            }
            return dragonsAlive;
        }

        public static void ChoosenOpenent(Character attacker, Character enemy)
        {
            Console.WriteLine($"Attacker {attacker.Name} choosen {enemy.Name} as an anemy");
        }
    }
}
