import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';

export default function HomeScreen({ navigation }) {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Smart Home Dashboard</Text>
      <Text style={styles.text}>Welcome to smart home dashboard! From here you will be able to access all your devices with these buttons:</Text>
      <TouchableOpacity 
        style={styles.button} 
        onPress={() => navigation.navigate('Lights')}
      >
        <Text style={styles.buttonText}>Go to Lights</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',   // keeps things centered horizontally
    justifyContent: 'flex-start', // push items to the top
    paddingTop: 50, // space from top
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 30,
  },
  text: {
    fontSize: 15,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 30,
  },
  button: {
    backgroundColor: '#4CAF50',
    padding: 15,
    borderRadius: 8,
  },
  buttonText: {
    color: 'white',
    fontSize: 18,
  },
});