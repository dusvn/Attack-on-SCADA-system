﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SimulatorPostrojenja.RealanSistem
{
    public class Uredjaj
    {
        TipUredjaja tipUredjaja;
        ushort vrednost;
        ushort minVrednost;
        ushort maxVrednost;

        public Uredjaj(TipUredjaja tu, ushort vr, ushort minvr, ushort maxvr)
        {
            tipUredjaja = tu;
            vrednost = vr;
            minVrednost = minvr;
            maxVrednost = maxvr;
        }

        public ushort Vrednost
        {
            get { return vrednost; }
            set 
            {
                if (value <= maxVrednost && value >= minVrednost)
                {
                    vrednost = value;
                }
            }
        }
    }
}
