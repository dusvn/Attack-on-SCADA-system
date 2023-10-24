using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace SimulatorPostrojenja.RealanSistem
{
    public class Postrojenje
    {
        public static ConcurrentDictionary<short, Uredjaj> sviUredjaji;

        private Thread simulatorThread;
        
        public Postrojenje()
        {
            sviUredjaji = new ConcurrentDictionary<short, Uredjaj>();
            sviUredjaji.GetOrAdd(30001, new Uredjaj(TipUredjaja.ANALOG_INPUT, 500, 100, 10000));
            sviUredjaji.GetOrAdd(1, new Uredjaj(TipUredjaja.DIGITAL_OUTPUT, 0, 0, 1));

            simulatorThread = new Thread(simulate);
            simulatorThread.Start();
        }

        private void simulate()
        {
            while (true)
            {
                if (sviUredjaji[1].Vrednost == 1)
                {
                    sviUredjaji[30001].Vrednost += 10;
                }
                else
                {
                    sviUredjaji[30001].Vrednost -= 1;
                }
                Thread.Sleep(1000);
            }
        }
    }
}
