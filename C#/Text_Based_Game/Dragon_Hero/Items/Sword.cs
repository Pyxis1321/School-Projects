using System;
using System.Collections.Generic;
using System.Text;

namespace Dragon_Hero.Items
{
    public class Sword : Items
    {
        public Sword(string itemName, int itemDamage, int itemWeight, int itemDefense = 0) : base(itemName, itemDamage, itemWeight, itemDefense)
        {

        }
    }
}
