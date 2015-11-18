using UnityEngine;
using System.Collections;

public class bodyMakerScript : MonoBehaviour {

	// Use this for initialization
	void Start () {
		InvokeRepeating ("makeBody", 0.0f, Camera.main.GetComponent<offsetValue> ().offset);
	}

	public Transform body;

	void makeBody(){
		Instantiate(body, new Vector3(0, 0, 0), Quaternion.identity);
	}
}
