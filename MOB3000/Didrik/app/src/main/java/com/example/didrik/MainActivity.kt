package com.example.didrika3

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.SmallFloatingActionButton
import androidx.compose.material3.Text
import androidx.compose.material3.TextField
import androidx.compose.material3.TextFieldDefaults
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.example.didrik.ui.theme.DidrikTheme


class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            DidrikTheme() {
                var screen by remember {
                    mutableStateOf("home")
                }
                if (screen==="home") {
                    Column(
                        horizontalAlignment = Alignment.CenterHorizontally,
                        modifier = Modifier
                            .fillMaxSize()

                    ) {
                        Row (
                            horizontalArrangement = Arrangement.SpaceEvenly,
                            modifier = Modifier
                                .fillMaxWidth()
                                .border(1.dp, Color.Black)
                                .padding(10.dp)
                        ) {
                            Text(text = "Home",
                                modifier = Modifier
                                    .clickable { screen = "home" })
                            Text(text = "Registrations"
                                , modifier = Modifier
                                    .clickable { screen = "registrations" })
                        }
                        Registration()
                    }
                }
                else if (screen==="registrations") {
                    Column(
                        horizontalAlignment = Alignment.CenterHorizontally,
                        modifier = Modifier
                            .fillMaxSize()

                    ) {
                        Navbar()
                        Text(text = "Registrations")
                    }
                }

            }


        }
    }
}

@Composable
fun Navbar(modifier: Modifier = Modifier) {
    Row (
        horizontalArrangement = Arrangement.SpaceEvenly,
        modifier = modifier
            .fillMaxWidth()
            .border(1.dp, Color.Black)
            .padding(10.dp)
    ) {
        Text(text = "Home",
            modifier = Modifier
                .clickable { screen = "home" })
        Text(text = "Registrations")
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun Registration() {
    var name by remember {
        mutableStateOf("")
    }

    var email by remember {
        mutableStateOf("")
    }


    Column(
        horizontalAlignment = Alignment.CenterHorizontally,
        modifier = Modifier
            .fillMaxSize()
    ) {
        Row(
            horizontalArrangement = Arrangement.SpaceEvenly,
            verticalAlignment = Alignment.CenterVertically,
            modifier = Modifier
                .fillMaxWidth()
                .padding(10.dp)
        ) {
            Column(
                verticalArrangement = Arrangement.SpaceEvenly
            ) {
                Text(
                    modifier = Modifier
                        .padding(0.dp,4.dp),
                    text = "Name:"
                )

                TextField(
                    value = name,
                    onValueChange = { newValue: String -> name = newValue},
                    colors = TextFieldDefaults.textFieldColors(textColor = Color.Black),
                    modifier = Modifier
                        .height(20.dp)
                )


                Text(
                    modifier = Modifier
                        .padding(0.dp,4.dp),
                    text = "Email:"
                )

                TextField(
                    value = email,
                    onValueChange = { newValue: String -> email = newValue },
                    colors = TextFieldDefaults.textFieldColors(textColor = Color.Black),
                    modifier = Modifier
                        .height(20.dp)
                )

            }

            SmallFloatingActionButton(
                onClick = {
                    null
                },
            ) {
                Text(text = "Register")
            }
        }
    }
}

@Preview(showBackground = true)
@Composable
fun GreetingPreview() {
    Column(
        horizontalAlignment = Alignment.CenterHorizontally,
        modifier = Modifier
            .fillMaxSize()

    ) {
        Navbar()
        Registration()
    }
}