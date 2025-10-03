// import { StatusBar } from 'expo-status-bar';
// import { StyleSheet, Text, View, TouchableOpacity } from 'react-native';
// import Slider from '@react-native-community/slider';
// import { useState } from 'react';

// export default function App() {

//   const [brightness, setBrightness] = useState(50);

//   const handleLightsOn = () => {
//     alert("Lights turned ON!");
//   };

//   const handleLightsOff = () => {
//     alert("Lights turned OFF!");
//   };

//   return (
//     <View style={styles.container}>
//       {/* Title */}
//       <Text style={styles.title}>Smart Home Dashboard</Text>

//       {/* Button Section */}
//       <View style={styles.buttonContainer}>
//         <TouchableOpacity style={styles.button} onPress={handleLightsOn}>
//           <Text style={styles.buttonText}>Lights On</Text>
//         </TouchableOpacity>

//         <TouchableOpacity style={styles.button} onPress={handleLightsOff} >
//           <Text style={styles.buttonText}>Lights Off</Text>
//         </TouchableOpacity>
//       </View>

//       {/* Slider for dimming lights */}
//       <View style={styles.sliderContainer}>
//         <Text>Brightness: {brightness}%</Text>
//         <Slider
//           style={{ width: 200, height: 40 }}
//           minimumValue={0}
//           maximumValue={100}
//           value={brightness}
//           onValueChange={value => setBrightness(Math.round(value))}
//           minimumTrackTintColor="#4CAF50"
//           maximumTrackTintColor="#E53935"
//           thumbTintColor="#000"
//         />
//       </View>

//       <StatusBar style="auto" />
//     </View>
//   );
// }

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     backgroundColor: '#fff',
//     alignItems: 'center',   // keeps things centered horizontally
//     justifyContent: 'flex-start', // push items to the top
//     paddingTop: 50, // space from top
//   },
//   title: {
//     fontSize: 24,
//     fontWeight: 'bold',
//     textAlign: 'center',
//     marginBottom: 30,
//   },
//   buttonContainer: {
//     alignSelf: 'flex-start', // aligns to left
//     marginLeft: 20,
//   },
//   button: {
//     backgroundColor: '#4CAF50', // green color
//     paddingVertical: 12,
//     paddingHorizontal: 20,
//     borderRadius: 8,
//     marginBottom: 10,
//   },
//   buttonText: {
//     fontSize: 18,
//     color: '#fff',
//     textAlign: 'center',
//   },
//   sliderContainer: {
//     alignItems: 'center',
//     marginTop: -100,
//   },
// });
import * as React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

// Import your screens
import HomeScreen from './screens/HomeScreen';
import LightsScreen from './screens/LightsScreen';

const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="Lights" component={LightsScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}