import dmxP512.*;
import processing.serial.*;

int values[];
int yellow[] = {59, 0, 0, 167, 0, 0, 0, 255};
int amber[] = {94, 0, 0, 78, 0,0,0, 255};

int nChannels = 8;
DmxP512 dmxOutput;
int universeSize=512;
String DMXPRO_PORT = "/dev/tty.usbserial-EN104384";
int DMXPRO_BAUDRATE =  115000;
int currentAdjustId = 0;
int mode = 1;
boolean showMix = false;


void setup() {
  size(255, 255);
  dmxOutput=new DmxP512(this, universeSize, true);
  dmxOutput.setupDmxPro(DMXPRO_PORT, DMXPRO_BAUDRATE);
  dmxOutput.setPriority(DmxP512.MAX_PRIORITY);
  print(dmxOutput);
  values = new int[nChannels];
  for (int i=0; i<nChannels; i++) {
    values[i] = 0;
  }
}

void draw() {
  background(64);
  if (mousePressed) {
    int value = constrain((int)map(mouseY, 0, height, 255, 0), 0, 255);
    values[currentAdjustId] = value;
  }
  for (int i=0; i<nChannels; i++) {
    fill(255);
    stroke(0);
    rect(i*(width/nChannels), height, (width/nChannels), 0-values[i]);
  }

  for (int i=0; i<nChannels; i++) {
    dmxOutput.set(i+1, values[i]); // don't send channel 0!
  }
  dmxOutput.set(8, 255);
}

void mousePressed() {
  currentAdjustId = constrain((int)map(mouseX, 0, width, 0, nChannels), 0, 6);
}

void keyPressed() {
  if ((key >= '1') && (key <= '7')) {
    currentAdjustId = (int)(key - '1');
    for (int i=0; i<=6; i++) {
      values[i] = (currentAdjustId == i) ? 255 : 0;
    }
  }
  if (key == ' ') {
    if (mode == 0) {
      showMix = !showMix;
      if (showMix) {
        for (int i=0; i<=6; i++) {
          values[i] = yellow[i];
        }
      } else {
        for (int i=0; i<=6; i++) {
          values[i] = 0;
        }
        values[1] = 40;
      }
    } else if (mode == 1){
      showMix = !showMix;
      if (showMix) {
        for (int i=0; i<=6; i++) {
          values[i] = amber[i];
        }
      } else {
        for (int i=0; i<=6; i++) {
          values[i] = 0;
        }
        values[2] = 99;
      }
    }
  }
  if (key == 'p') {
    println("----");
    printArray(values);
  }




  if (key == 'S') {
    for (int i=0; i<=6; i++) {
      if (mode == 0) {
        yellow[i] = values[i];
      } else if (mode == 1){
        amber[i] = values[i];
      }
    }
  }

  if (key == 'm'){
      mode = 1-mode; 
  }



  if (key == 'w') {
    for (int i=0; i<=6; i++) {
      values[i] = 0;
    }
    values[1]=115;
    values[6]=146;
  }
  if (key == 'W') {
    for (int i=0; i<=6; i++) {
      values[i] = 0;
    }
    values[0]=166;
    values[4]=255;
  }
}
