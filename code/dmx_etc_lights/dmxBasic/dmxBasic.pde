import dmxP512.*;
import processing.serial.*;

int values[];
int nChannels = 8;
DmxP512 dmxOutput;
int universeSize=512;
String DMXPRO_PORT = "/dev/tty.usbserial-EN104384";
int DMXPRO_BAUDRATE =  115000;

void setup() {
  size(255, 255);
  dmxOutput=new DmxP512(this, universeSize, true);
  dmxOutput.setupDmxPro(DMXPRO_PORT, DMXPRO_BAUDRATE);
  dmxOutput.setPriority(DmxP512.MAX_PRIORITY);
  print(dmxOutput);
  values = new int[nChannels];
  for (int i=0; i<nChannels; i++) {values[i] = 0; }
}

void draw() {
  background(44);
  if (mousePressed) {
    int channel = constrain((int)map(mouseX, 0, width, 0, nChannels),0,6);
    int value = constrain((int)map(mouseY, 0, height, 255, 0),0,255);
    values[channel] = value;
    dmxOutput.set(channel+1, value); // don't send channel 0!
  }
  for (int i=0; i<nChannels; i++) {
    fill(255);
    rect(i*(width/nChannels), height, width/nChannels, 0-values[i]);
  }
  dmxOutput.set(8, 255);
}
