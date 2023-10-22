using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;

namespace SimulatorPostrojenja.ModbusStvari
{
    public class ModbusPaket
    {
        private ushort transactionId;
        private ushort protocolId;
        private ushort length;
        private byte unitId;
        private byte functionCode;
        private byte[] data;

        public ModbusPaket(byte[] paketSaNeta)
        {
            transactionId = (ushort)IPAddress.NetworkToHostOrder((short)BitConverter.ToUInt16(paketSaNeta, 0));
            protocolId = (ushort)IPAddress.NetworkToHostOrder((short)BitConverter.ToUInt16(paketSaNeta, 2));
            length = (ushort)IPAddress.NetworkToHostOrder((short)BitConverter.ToUInt16(paketSaNeta, 4));
            unitId = paketSaNeta[6];
            functionCode = paketSaNeta[7];
            data = new byte[paketSaNeta.Length - 8];
            Buffer.BlockCopy(paketSaNeta, 8, data, 0, paketSaNeta.Length - 8);
        }

        public byte[] BajtoviIzPaketa()
        {
            byte[] bajtovi = new byte[length + 6];
            Buffer.BlockCopy(BitConverter.GetBytes(transactionId), 0, bajtovi, 0, 2);
            Buffer.BlockCopy(BitConverter.GetBytes(protocolId), 0, bajtovi, 2, 2);
            Buffer.BlockCopy(BitConverter.GetBytes(length), 0, bajtovi, 4, 2);
            bajtovi[6] = unitId;
            bajtovi[7] = functionCode;
            Buffer.BlockCopy(data, 0, bajtovi, 8, length - 1);
            return bajtovi;
        }
    }
}
