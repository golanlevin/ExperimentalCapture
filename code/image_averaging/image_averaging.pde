int nImages = 0;
PImage images[];
int nPixels;
float averageImagef [][];
color averagedPixelColors[];

// Image averaging (a la Jason Salavon)
// Known to work with Processing 3.0.1
// Golan Levin, 2011

//======================================
void setup(){
  size(240, 240);
  nPixels = width*height;

  initializeArrays();
  loadImages();
  computeAverageImage();
}

//======================================
void draw(){
  loadPixels();
  for (int i=0; i<nPixels; i++){
    pixels[i] = averagedPixelColors[i];
  }
  updatePixels();
}

//======================================
void  initializeArrays(){
  // make and clear the average image
  averageImagef = new float[nPixels][3]; 
  averagedPixelColors = new color[nPixels];
  for (int i=0; i<nPixels; i++){
    averageImagef[i][0] = 0;
    averageImagef[i][1] = 0;
    averageImagef[i][2] = 0;
  }
}

//======================================
void loadImages(){
  // This function loads and counts 
  // all of the (image) files in the data folder.
  
  // Images should all be the same size. If they're not, 
  // or if any of them are smaller than the width&height,
  // then you may get an arrayOutOfBoundsException.

  // See http://www.flickr.com/groups/circle/pool/
  // String folderPath = selectFolder(); // choose manually, or..

  String dataFolderPath = dataPath("");
  File myDataFolder = new File(dataFolderPath);

  String[] imageFilenames = myDataFolder.list();
  if (imageFilenames != null) {
    nImages = imageFilenames.length;
    images = new PImage[nImages];
    
    int count = 0; 
    for (int i=0; i<nImages; i++) {
      String filename = imageFilenames[i];
      if (filename.endsWith(".jpg")){
        images[count] = loadImage(filename);
        count++;
      }
    }
    nImages = count;
  }
}


//======================================
void computeAverageImage(){
  if (nImages > 0){

    for (int i=0; i<nPixels; i++){              // for each pixel
      for (int j=0; j<nImages; j++){            // for each image
        color c = images[j].pixels[i];          // get the color of that pixel in that image
        float r = red   (c);                    // extract the color components of that pixel
        float g = green (c);
        float b = blue  (c);
        averageImagef[i][0] += r;               // sum (accumulate) the color components
        averageImagef[i][1] += g;
        averageImagef[i][2] += b;
      }
    }
    
    
    for (int i=0; i<nPixels; i++){
       // divide the sums by the number of images, to get averages
      averageImagef[i][0] /= (float)nImages;
      averageImagef[i][1] /= (float)nImages;
      averageImagef[i][2] /= (float)nImages;
      
      // create and store new colors from these averages
      float r = averageImagef[i][0];
      float g = averageImagef[i][1];
      float b = averageImagef[i][2];
      averagedPixelColors[i] = color (r,g,b); 
    }
 
    
  }
}