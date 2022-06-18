using Dragon_Hero.Characters;
using System;
using System.Collections.Generic;
using System.Text;

namespace Dragon_Hero.Items
{
    public class Items
    {
        public string ItemName { get; set; }
        public int ItemDamage { get; set; }
        public int ItemDefense { get; set; }
        public int ItemWeight { get; set; }
        public Items(string itemName, int itemDamage, int itemDefense, int itemWeight)
        {
            this.ItemName = itemName;
            this.ItemDamage = itemDamage;
            this.ItemDefense = itemDefense;
            this.ItemWeight = itemWeight;
        }
    }
    
}
