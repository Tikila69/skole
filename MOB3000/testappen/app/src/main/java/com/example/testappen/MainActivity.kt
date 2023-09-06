package com.example.testappen

import android.graphics.Matrix
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.google.android.material.floatingactionbutton.FloatingActionButton



class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.layout) // Replace with your layout name
        val menubutton = findViewById<FloatingActionButton>(R.id.menuDropdown)
        menubutton.setOnClickListener{
            // Create a matrix for the rotation transformation
            val matrix = Matrix()
            matrix.postRotate(180F, menubutton.width / 0F, menubutton.height / 0F)

            // Apply the rotation to the button
            menubutton.imageMatrix = matrix
        }



        // Any additional initialization or setup code can go here
    }

    // You can add more functions to handle UI interactions or other tasks

}