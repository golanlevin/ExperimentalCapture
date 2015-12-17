#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup(){
    ofSetFrameRate(60);
    ofSetVerticalSync(true);
    ofEnableDepthTest();

    tempMesh = ofVboMesh();
    
    tempMesh.setMode(OF_PRIMITIVE_POINTS);
    tempMesh.load("church-mesh.ply") ; // change for different data set
    
    imgCount = 0 ;
    
    cam.setFarClip(100000) ;
    cam.setNearClip(0.1) ;
}

//--------------------------------------------------------------
void ofApp::update(){
}

//--------------------------------------------------------------
void ofApp::draw(){
    ofBackgroundGradient(ofColor::gray, ofColor::black);
    
    cam.begin();
        ofPushMatrix();
        ofScale(200, 200, 200); // change depending on data set
        tempMesh.draw() ;
        ofPopMatrix();
    cam.end() ;
    
    if(ofGetKeyPressed()){
        ofDrawBitmapStringHighlight(ofToString(ofGetFrameRate()), 50, 50);
    }
}

//--------------------------------------------------------------
void ofApp::keyPressed(int key){
    if (key == 99) { // if 'c' pressed take a screenshot
        ofSaveScreen("screencaptures/frame_" + ofToString(imgCount) + ".png");
        imgCount++;
    }
}

//--------------------------------------------------------------
void ofApp::keyReleased(int key){
    
}

//--------------------------------------------------------------
void ofApp::mouseMoved(int x, int y ){
    
}

//--------------------------------------------------------------
void ofApp::mouseDragged(int x, int y, int button){
    
}

//--------------------------------------------------------------
void ofApp::mousePressed(int x, int y, int button){
    
}

//--------------------------------------------------------------
void ofApp::mouseReleased(int x, int y, int button){
    
}

//--------------------------------------------------------------
void ofApp::windowResized(int w, int h){
    
}

//--------------------------------------------------------------
void ofApp::gotMessage(ofMessage msg){
    
}

//--------------------------------------------------------------
void ofApp::dragEvent(ofDragInfo dragInfo){ 
    
}
