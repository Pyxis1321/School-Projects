using System;
using System.Collections.Generic;
using System.Text;

namespace Dragon_Hero.Randomness
{
    static class ColorfullConsole
    {
        private static readonly ConsoleColor initialColor; 
        public static ConsoleColor InitialColor
        {
            get
            {
                return initialColor;
            }
        }

        static ColorfullConsole()
        {
            ColorfullConsole.initialColor = ConsoleColor.Gray;
        }

        public static void WriteLine(string text, ConsoleColor color)
        {
            ConsoleColor initail = Console.ForegroundColor;
            Console.ForegroundColor = color;
            Console.WriteLine(text);
            Console.ForegroundColor = initail;
        }

        public static void Write(string text, ConsoleColor color)
        {
            ConsoleColor initail = Console.ForegroundColor;
            Console.ForegroundColor = color;
            Console.WriteLine(text);
            Console.ForegroundColor = initail;
        }
    }
}
