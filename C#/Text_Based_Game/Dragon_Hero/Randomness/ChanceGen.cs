using System;
using System.Collections.Generic;
using System.Text;

namespace Dragon_Hero.Randomness
{
    public class ChanceGen : Random
    {
        private static ChanceGen instance;
        public static ChanceGen Instance
        {
            get
            {
                if (instance == null)
                    instance = new ChanceGen();

                return instance;
            }
        }

        private ChanceGen()
        {

        }
    }
}
