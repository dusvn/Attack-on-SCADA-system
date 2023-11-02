using SimulatorPostrojenja.ModbusStvari;
using SimulatorPostrojenja.RealanSistem;
using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;

namespace SimulatorPostrojenja.Obradjivaci
{
    public class IzvrsilacFunkcije
    {   
        public IzvrsilacFunkcije()
        {

        }

        public byte[] napraviResponse(ModbusPaket mbp)
        {
            if (mbp.FunctionCode >= 1 && mbp.FunctionCode <= 4)
            {
                ModbusReadRequest mbrq = new ModbusReadRequest(mbp);
                if (mbp.FunctionCode == 1 || mbp.FunctionCode == 2)
                {
                    return procitajDigital(mbrq);
                }
                else return procitajAnalog(mbrq);
            }
            else if (mbp.FunctionCode == 5 || mbp.FunctionCode == 6)
            {
                ModbusWriteRequest mbwq = new ModbusWriteRequest(mbp);
                if (mbp.FunctionCode == 5)
                {
                    return zapisiDigital(mbwq);
                }
                else return zapisiAnalog(mbwq);
            }
            else return null;
        }

        byte[] procitajDigital(ModbusReadRequest mbrq)
        {
            if(mbrq.QuantityToRead > 2000 || mbrq.QuantityToRead < 1)
            {
                return null;
            }
            if (!Postrojenje.sviUredjaji.ContainsKey((ushort)mbrq.StartingAddress))
            {
                return null;
            }
            List<ushort> vrednosti = new List<ushort>();
            for (int i = 0; i < mbrq.QuantityToRead; ++i)
            {
                Uredjaj u = Postrojenje.sviUredjaji[(ushort)(mbrq.StartingAddress + i)];
                if (u.TipUredjaja != TipUredjaja.DIGITAL_INPUT && u.TipUredjaja != TipUredjaja.DIGITAL_OUTPUT)
                {
                    return null;
                }
                vrednosti.Add(u.Vrednost);
            }
            byte[] odgovor = mbrq.pakujDigitalRead(vrednosti);
            return odgovor;
        }

        byte[] procitajAnalog(ModbusReadRequest mbrq)
        {
            if (mbrq.QuantityToRead > 125 || mbrq.QuantityToRead < 1)
            {
                return null;
            }
            if (!Postrojenje.sviUredjaji.ContainsKey((ushort)mbrq.StartingAddress))
            {
                return null;
            }
            List<ushort> vrednosti = new List<ushort>();
            for (int i = 0; i < mbrq.QuantityToRead; ++i)
            {
                Uredjaj u = Postrojenje.sviUredjaji[(ushort)(mbrq.StartingAddress + i)];
                if(u.TipUredjaja != TipUredjaja.ANALOG_INPUT && u.TipUredjaja != TipUredjaja.ANALOG_OUTPUT)
                {
                    return null;
                }
                vrednosti.Add(u.Vrednost);
            }
            //odgovor
            byte[] odgovor = mbrq.pakujAnalogRead(vrednosti);
            return odgovor;
        }

        byte[] zapisiDigital(ModbusWriteRequest mbwq)
        {
            if(mbwq.OutputValue != 0xFF00 && mbwq.OutputValue != 0x0000)
            {
                return null;
            }
            if (!Postrojenje.sviUredjaji.ContainsKey(mbwq.OutputAddress))
            {
                return null;
            }
            if(Postrojenje.sviUredjaji[mbwq.OutputAddress].TipUredjaja != TipUredjaja.DIGITAL_OUTPUT)
            {
                return null;
            }
            Postrojenje.sviUredjaji[mbwq.OutputAddress].Vrednost = mbwq.OutputValue == 0 ? (ushort)0 : (ushort)1;
            byte[] odgovor = mbwq.pakujDigitalWrite();
            return odgovor;
        }

        byte[] zapisiAnalog(ModbusWriteRequest mbwq)
        {
            if (!Postrojenje.sviUredjaji.ContainsKey(mbwq.OutputAddress))
            {
                return null;
            }
            if (Postrojenje.sviUredjaji[mbwq.OutputAddress].TipUredjaja != TipUredjaja.ANALOG_OUTPUT)
            {
                return null;
            }
            Postrojenje.sviUredjaji[mbwq.OutputAddress].Vrednost = mbwq.OutputValue;
            byte[] odgovor = mbwq.pakujAnalogWrite();
            return odgovor;
        }
    }
}
