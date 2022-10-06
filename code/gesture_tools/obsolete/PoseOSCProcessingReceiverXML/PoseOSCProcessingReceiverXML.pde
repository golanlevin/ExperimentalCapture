import java.util.Map;
import oscP5.*;
OscP5 oscP5;
// Be sure to set the 'format' in PoseOSC to XML
 
public class Keypoint{
  PVector position;
  float score;
  public Keypoint(){
    this.position = new PVector(0,0);
    this.score = 0;
  }
}
public class Pose{
  HashMap<String,Keypoint> keypoints;
  float score;
  public Pose(){
    this.keypoints = new HashMap<String,Keypoint>();
    this.score = 0;
  }
}
Pose[] poses = new Pose[0];
int nPoses = 0;

//----------------------------------
void setup() {
  size(640,480);
  //fullScreen();
  OscProperties myProperties = new OscProperties();
  // increase the datagram size to 10000 bytes
  // by default it is set to 1536 bytes
  // https://processing.org/discourse/beta/num_1189011577.html
  myProperties.setDatagramSize(10000); 
  myProperties.setListeningPort(9527);
  
  oscP5 = new OscP5(this, myProperties);
  oscP5.plug(this,"parseData","/poses/xml"); 
}

void drawBone(Pose pose, String part0, String part1){
  HashMap<String,Keypoint> keypoints;
  try{
    keypoints = pose.keypoints;
  }catch(Exception e){
    return;//meh
  }
  if (!keypoints.containsKey(part0)){
    return;
  }
  if (!keypoints.containsKey(part1)){
    return;
  }

  PVector p0 = keypoints.get(part0).position;
  PVector p1 = keypoints.get(part1).position;
  line(p0.x,p0.y,p1.x,p1.y);
  
}

 
//----------------------------------
void draw() {
  background (180);
  fill(0);
  stroke(0);
  for (int i = 0; i < nPoses; i++){
    drawBone(poses[i],"leftShoulder","rightShoulder");
    drawBone(poses[i],"leftHip","rightHip");
    drawBone(poses[i],"leftShoulder","leftHip");
    drawBone(poses[i],"rightShoulder","rightHip");
    drawBone(poses[i],"leftShoulder","leftElbow");
    drawBone(poses[i],"rightShoulder","rightElbow");
    drawBone(poses[i],"leftElbow","leftWrist");
    drawBone(poses[i],"rightElbow","rightWrist");
    drawBone(poses[i],"leftHip","leftKnee");
    drawBone(poses[i],"rightHip","rightKnee");
    drawBone(poses[i],"leftKnee","leftAnkle");
    drawBone(poses[i],"rightKnee","rightAnkle");
    drawBone(poses[i],"nose","leftEye");
    drawBone(poses[i],"nose","rightEye");
    drawBone(poses[i],"leftEye","leftEar");
    drawBone(poses[i],"rightEye","rightEar");
  }
}
 
//----------------------------------
public void parseData(String data){
  
  XML xml = parseXML(data);
  nPoses = xml.getInt("nPoses");
  int w = xml.getInt("videoWidth");
  int h = xml.getInt("videoHeight");
  
  if (w != width || h != height){
    surface.setSize(w,h);
  }
  
  poses = new Pose[nPoses];
  XML[] xmlposes = xml.getChildren("pose");
  for (int i = 0; i < xmlposes.length; i++){
    XML[] xmlkeypoints = xmlposes[i].getChildren("keypoint");
    
    poses[i] = new Pose();
    poses[i].score = xmlposes[i].getFloat("score");
    
    for (int j = 0; j < xmlkeypoints.length; j++){
      Keypoint kpt = new Keypoint();
     
      kpt.position.x = xmlkeypoints[j].getFloat("x");
      kpt.position.y = xmlkeypoints[j].getFloat("y");
      kpt.score = xmlkeypoints[j].getFloat("score");
      
      poses[i].keypoints.put(xmlkeypoints[j].getString("part"), kpt);
    }
  }

}
