﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;
using SimulatorPostrojenja.ModbusStvari;
using SimulatorPostrojenja.RealanSistem;

namespace SimulatorPostrojenja
{
    class Program
    {
        static void Main(string[] args)
        {
            Postrojenje postrojenje = new Postrojenje();
            using(Socket socket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp))
            {
                IPAddress adresa = IPAddress.Loopback;
                IPEndPoint adresaIPort = new IPEndPoint(adresa, 25252);
                socket.Bind(adresaIPort);
                socket.Listen(1);
                Socket acceptSocket = socket.Accept();

                while (true)
                {
                    primiPaket(acceptSocket);
                }

                //obradiPoruku();
                //IzvrsiKomanduIzPoruke(poruka);
            }
        }

        static void primiPaket(Socket acceptSocket)
        {
            byte[] mbapHeader = new byte[7];
            acceptSocket.Receive(mbapHeader, 7, SocketFlags.None);
            int velicinaPaketa = 0;
            unchecked
            {
                velicinaPaketa = IPAddress.NetworkToHostOrder((short)BitConverter.ToUInt16(mbapHeader, 4));
            }
            byte[] podaci = new byte[velicinaPaketa - 1];
            acceptSocket.Receive(podaci, velicinaPaketa - 1, SocketFlags.None); //minus jedan jer smo izvukli ceo mrtvi heder a length polje u sebi sadrzi 1 bajt iz hedera, koji smo jelte izvukli
            byte[] ceoPaket = new byte[7 + velicinaPaketa - 1];
            Buffer.BlockCopy(mbapHeader, 0, ceoPaket, 0, 7);
            Buffer.BlockCopy(podaci, 0, ceoPaket, 7, velicinaPaketa - 1);

            ModbusPaket primljeniPaket = new ModbusPaket(ceoPaket);
            if(primljeniPaket.FunctionCode>= 1 && primljeniPaket.FunctionCode <= 4)
            {
                procitajVrednost(primljeniPaket);
            } else if(primljeniPaket.FunctionCode >=5 && primljeniPaket.FunctionCode <= 6)
            {
                zapisiVrednost(primljeniPaket);
            }
            else
            {
                //greska
            }
        }
    }
}
