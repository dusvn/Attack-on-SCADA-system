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
        public static ConcurrentDictionary<ushort, Uredjaj> sviUredjaji;

        private Thread simulatorThread;
        
        public Postrojenje()
        {
            sviUredjaji = new ConcurrentDictionary<ushort, Uredjaj>();
            sviUredjaji.GetOrAdd(2000, new Uredjaj(TipUredjaja.ANALOG_INPUT, 500, 100, 10000));
            sviUredjaji.GetOrAdd(1000, new Uredjaj(TipUredjaja.DIGITAL_OUTPUT, 1, 0, 1));

            simulatorThread = new Thread(simulate);
            simulatorThread.Start();
        }

        private void simulate()
        {
            while (true)
            {
                if (sviUredjaji[1000].Vrednost == 1)
                {
                    sviUredjaji[2000].Vrednost += 10;
                }
                else
                {
                    sviUredjaji[2000].Vrednost -= 1;
                }
                Thread.Sleep(1000);
            }
        }
    }
}
