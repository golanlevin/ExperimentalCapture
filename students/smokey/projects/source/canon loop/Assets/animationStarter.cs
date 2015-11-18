using UnityEngine;
using System.Collections;

public class animationStarter : MonoBehaviour {

	private float offset;
	public int myCount = 0;
	private float a=255;

	// Use this for initialization
	void Start () {
		offset = Camera.main.GetComponent<offsetValue>().offset;
		gameObject.GetComponent<Animator>().speed = 0.0f;
		Invoke ("startAnimation", offset * myCount);
		InvokeRepeating ("fade", Camera.main.GetComponent<offsetValue> ().offset * 5 - 1, 0.02f);
		Destroy (gameObject, Camera.main.GetComponent<offsetValue>().offset*5);
	}

   void startAnimation(){
		gameObject.GetComponent<Animator>().speed = 1.0f;
	}

	void fade(){
		a -= 100;
		if (a < 0) {
			a = 0;
		}
		Color myColor = gameObject.GetComponentInChildren<Renderer> ().material.color;
		Color myNewColor = new Color (myColor.r, myColor.g, myColor.b, a);
		gameObject.GetComponentInChildren<Renderer> ().material.SetColor ("mainColor", myNewColor);
	}
}
