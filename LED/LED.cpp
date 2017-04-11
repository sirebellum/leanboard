#include <iostream>
#include <errno.h>
#include <linux/spi/spidev.h>
#include <unistd.h>

using namespace std;

int main()
{
   int fd, result;
   unsigned char buffer[100];

   cout << "Initializing" << endl ;

   // Configure the interface.
   // CHANNEL insicates chip select,
   // 500000 indicates bus speed.
   fd = wiringPiSPISetup(0, 50000);

   cout << "Init result: " << fd << endl;

   buffer[0] = 0x25;
   buffer[1] = 0x16;
   buffer[2] = 0x7F;
   buffer[3] = 0x7F;
   buffer[4] = 0x7F;
   buffer[5] = 0xFF;
   wiringPiSPIDataRW(0, buffer, 6);


   sleep(5);


}