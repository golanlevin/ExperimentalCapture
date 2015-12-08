#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup(){

    ofSetFrameRate(15);
    
    model.loadModel("monisha.dae");
    centerPos.set(0, 100, 0);
    bgImage.loadImage("background.jpg");
}

//--------------------------------------------------------------
void ofApp::update(){

}

//--------------------------------------------------------------
void ofApp::draw(){
    
    ofSetColor(255);
    ofBackground(250);
    bgImage.draw(0, 0, ofGetWidth(), ofGetHeight());
    
    ofEnableDepthTest();
    
    cam.begin();

    ofPushMatrix();
    ofScale(-1, -1, 1);
    ofTranslate(centerPos.x, centerPos.y, centerPos.z);
    model.drawFaces();
    ofPopMatrix();

    cam.end();
    
    ofDisableDepthTest();

    ofSetColor(255);
    ofDrawBitmapString("Press 'r' to reset the camera", 10, ofGetHeight() - 16);
    ofDrawBitmapString("Rotate with left mouse button", 10, ofGetHeight() - 32);
    ofDrawBitmapString("Zoom with right mouse button", 10, ofGetHeight() - 48);
    ofDrawBitmapString("Pan with option + left mouse button", 10, ofGetHeight() - 64);
}

//--------------------------------------------------------------
void ofApp::keyPressed(int key){
    switch(key) {
        case 'r':
            cam.reset();
            break;
        default:
            break;
    }
}

//--------------------------------------------------------------
void ofApp::keyReleased(int key){
    //
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

