using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;

namespace SimulatorPostrojenja.ModbusStvari
{
    public class ModbusWriteRequest : ModbusPaket
    {
        ushort outputAddress;
        ushort outputValue;

        public ModbusWriteRequest(ModbusPaket mbp) : base(mbp)
        {
            outputAddress = (ushort)IPAddress.NetworkToHostOrder((short)BitConverter.ToUInt16(mbp.Data, 0));
            outputValue = (ushort)IPAddress.NetworkToHostOrder((short)BitConverter.ToUInt16(mbp.Data, 2));
        }
    }
}
