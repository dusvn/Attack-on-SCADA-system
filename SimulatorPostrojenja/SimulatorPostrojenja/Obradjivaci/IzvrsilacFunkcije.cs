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
            } /*
            else if (mbp.FunctionCode == 5 || mbp.FunctionCode == 6)
            {
                ModbusWriteRequest mbwq = new ModbusWriteRequest(mbp);
                if (mbp.FunctionCode == 5)
                {
                    return zapisiAnalog(mbwq);
                }
                else return zapisiDigital(mbwq);
            } */
            else return null;
        }

        byte[] procitajDigital(ModbusReadRequest mbrq)
        {
            if(mbrq.QuantityToRead > 2000 || mbrq.QuantityToRead < 1)
            {
                return null;
            }
            if (!Postrojenje.sviUredjaji.ContainsKey((short)mbrq.StartingAddress))
            {
                return null;
            }
            List<ushort> vrednosti = new List<ushort>();
            for (int i = 0; i < mbrq.QuantityToRead; ++i)
            {
                Uredjaj u = Postrojenje.sviUredjaji[(short)(mbrq.StartingAddress + i)];
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
            if (!Postrojenje.sviUredjaji.ContainsKey((short)mbrq.StartingAddress))
            {
                return null;
            }
            List<ushort> vrednosti = new List<ushort>();
            for (int i = 0; i < mbrq.QuantityToRead; ++i)
            {
                Uredjaj u = Postrojenje.sviUredjaji[(short)(mbrq.StartingAddress + i)];
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
    }
}
