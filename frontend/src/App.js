// src/App.js
import React, { useState } from 'react';
import { GoogleOAuthProvider } from '@react-oauth/google';
import GoogleLoginComponent from './components/GoogleLoginComponent';
import axios from 'axios';
import './App.css';

function App() {
    const googleClientId = '960344337123-saaspt04lo9edrtjhifd9gpmjrjijjn3.apps.googleusercontent.com'; // Replace with your Google Client ID

    // State to handle DB connection status
    const [dbStatus, setDbStatus] = useState(null);
    const [dbMessage, setDbMessage] = useState('');

    // Function to test the DB connection
    const testDbConnection = async () => {
        try {
            const response = await axios.get('/test-db-connection');  // Your API endpoint to test DB connection
            setDbStatus('success');
            setDbMessage(response.data.message || 'Database connected successfully!');
        } catch (error) {
            setDbStatus('error');
            setDbMessage(error.response ? error.response.data.message : 'Error connecting to the database');
        }
    };

    return (
        <GoogleOAuthProvider clientId={googleClientId}>
            <div className="App">
                {/* Google Login Component */}
                <GoogleLoginComponent />
            </div>
        </GoogleOAuthProvider>
    );
}

export default App;
