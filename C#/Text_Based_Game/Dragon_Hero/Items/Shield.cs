using System;
using System.Collections.Generic;
using System.Text;

namespace Dragon_Hero.Items
{
    public class Shield : Items
    {
        public Shield(string itemName, int itemDefense, int itemWeight, int itemDamage = 0) : base(itemName, itemDamage, itemDefense, itemWeight)
        {

        }
    }
}
