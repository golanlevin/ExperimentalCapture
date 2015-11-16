#include "ofApp.h"

//--------------------------------------------------------------
void saveMeshes(vector<ofMesh> meshes, string sceneName) {
    meshes[0].save("saved/" + sceneName + "_scanX.ply");
    ofLog() << "Saved " + sceneName + "_scanX.ply";
    meshes[1].save("saved/" + sceneName + "_scanY.ply");
    ofLog() << "Saved " + sceneName + "_scanY.ply";
    meshes[2].save("saved/" + sceneName + "_scanZ.ply");
    ofLog() << "Saved " + sceneName + "_scanZ.ply";
}

//--------------------------------------------------------------
vector<ofMesh> slitScanFromDirectory(string sceneName, float minX, float maxX,
                                     float minY, float maxY, float minZ, float maxZ) {
    // Get directory listings from scene name
    ofDirectory dir(sceneName + "/");
    dir.allowExt("ply");
    dir.listDir();
    
    // Compute slice lengths
    float sliceX = (maxX - minX) / dir.size();
    float sliceY = (maxY - minY) / dir.size();
    float sliceZ = (maxZ - minZ) / dir.size();
    
    // Set up meshScans
    vector<ofMesh> meshScans;
    ofMesh meshScanX;
    ofMesh meshScanY;
    ofMesh meshScanZ;
    meshScanX.setMode(OF_PRIMITIVE_POINTS);
    meshScanY.setMode(OF_PRIMITIVE_POINTS);
    meshScanZ.setMode(OF_PRIMITIVE_POINTS);
    
    // Iterate through ply files
    for (int i = 0; i < dir.size(); i++) {
        ofLog() << "Scanning " << sceneName << " frame" << i << "...";
        ofMesh tempMesh;
        tempMesh.setMode(OF_PRIMITIVE_POINTS);
        tempMesh.load(dir.getPath(i));
        
        // Filter through vertices
        for (int j = 0; j < tempMesh.getVertices().size(); j++) {
            ofVec3f tempVertex = tempMesh.getVertex(j);
            
            // Slitscan x-axis
            float lowX = minX + (sliceX * i);
            float highX = lowX + sliceX;
            if ((lowX < tempVertex.x) & (tempVertex.x < highX) ) {
                meshScanX.addColor(tempMesh.getColor(j));
                meshScanX.addVertex(tempVertex);
            }
            
            // Slitscan y-axis
            float lowY = minY + (sliceY * i);
            float highY = lowY + sliceY;
            if ((lowY < tempVertex.y) & (tempVertex.y < highY) ) {
                meshScanY.addColor(tempMesh.getColor(j));
                meshScanY.addVertex(tempVertex);
            }
            
            // Slitscan z-axis
            float lowZ = minZ + (sliceZ * i);
            float highZ = lowZ + sliceZ;
            if ((lowZ < tempVertex.z) & (tempVertex.z < highZ) ) {
                meshScanZ.addColor(tempMesh.getColor(j));
                meshScanZ.addVertex(tempVertex);
            }
        }
    }
    
    // Add the meshes to the meshScan
    meshScans.push_back(meshScanX);
    meshScans.push_back(meshScanY);
    meshScans.push_back(meshScanZ);
    
    // Save out the meshes
    saveMeshes(meshScans, sceneName);
    
    // Return the meshScans
    return meshScans;
}

//--------------------------------------------------------------
void ofApp::setup(){

    // General settings
    ofSetFrameRate(24);
    ofSetVerticalSync(true);
    ofEnableDepthTest();
    glEnable(GL_POINT_SMOOTH);
    glPointSize(1);
    numScenes = 6;
    
    // Load the meshes if they are already saved
    ofDirectory dir("saved/");
    dir.allowExt("ply");
    dir.listDir();
    
    if (dir.size() == numScenes * 3) {
        for (int i = 0; i < numScenes; i++) {
            ofLog() << "Loading ply for scene " + ofToString(i) + "...";
            
            ofMesh tempMeshX;
            tempMeshX.setMode(OF_PRIMITIVE_POINTS);
            tempMeshX.load("saved/scene" + ofToString(i) + "_scanX.ply");
            meshes.push_back(tempMeshX);
            
            ofMesh tempMeshY;
            tempMeshY.setMode(OF_PRIMITIVE_POINTS);
            tempMeshY.load("saved/scene" + ofToString(i) + "_scanY.ply");
            meshes.push_back(tempMeshY);
            
            ofMesh tempMeshZ;
            tempMeshZ.setMode(OF_PRIMITIVE_POINTS);
            tempMeshZ.load("saved/scene" + ofToString(i) + "_scanz.ply");
            meshes.push_back(tempMeshZ);
        }
    } else {
        // Choose xyz bounds
        float minX = -2.45;
        float maxX = 2.15;
        float minY = -1.125;
        float maxY = 0.8;
        float minZ = 0;
        float maxZ = 4.9;
        
        // Process slit scans for each directory
        for (int i = 0; i < numScenes; i++) {
            string sceneName = "scene" + ofToString(i);
            vector<ofMesh> tempMeshes = slitScanFromDirectory(sceneName, minX, maxX, minY,
                                                              maxY, minZ, maxZ);
            meshes.push_back(tempMeshes[0]);
            meshes.push_back(tempMeshes[1]);
            meshes.push_back(tempMeshes[2]);
        }
    }
    
    // For displaying the meshes
    sceneIndex = 0;
    currentAxis = "X";
    drawMesh = meshes[sceneIndex];
}

//--------------------------------------------------------------
void ofApp::update(){
    
}

//--------------------------------------------------------------
void ofApp::draw(){
    ofBackgroundGradient(ofColor::gray, ofColor::black, OF_GRADIENT_CIRCULAR);
    
    cam.begin();
    ofScale(90, 90, 90);
    drawMesh.draw();
    cam.end();
    
    string textLabel = "Scene: " + ofToString(sceneIndex) + " Scan: " + currentAxis;
    if (sceneIndex == 0) {
        textLabel = "<Test Scene> Scan: " + currentAxis;
    }
    ofDrawBitmapString(textLabel, 20, ofGetHeight() - 20);
}

//--------------------------------------------------------------
void ofApp::keyPressed(int key){
    // Display the slit scans according to scene number and current axis
    if ((0 < key - 48) & (key - 48 < numScenes)) {
        sceneIndex = key - 48;
        drawMesh = meshes[sceneIndex * 3];
        currentAxis = "X";
    } else {
        switch(key) {
            case 'x':
                drawMesh = meshes[sceneIndex * 3];
                currentAxis = "X";
                break;
            case 'y':
                drawMesh = meshes[sceneIndex * 3 + 1];
                currentAxis = "Y";
                break;
            case 'z':
                drawMesh = meshes[sceneIndex * 3 + 2];
                currentAxis = "Z";
                break;
            case OF_KEY_BACKSPACE:
                cam.reset();
                break;
            default:
                break;
        }
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
void ofApp::mouseEntered(int x, int y){
    
}

//--------------------------------------------------------------
void ofApp::mouseExited(int x, int y){
    
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
