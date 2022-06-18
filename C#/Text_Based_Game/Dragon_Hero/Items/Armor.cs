using System;
using System.Collections.Generic;
using System.Text;

namespace Dragon_Hero.Items
{
    public class Armor : Items
    {
        public Armor(string itemName, int itemDamage, int itemWeight, int itemDefense = 0) : base(itemName, itemDamage, itemWeight, itemDefense)
        {

        }
    }
}
