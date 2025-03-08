// src/components/GoogleLoginComponent.js
import React from 'react';
import { GoogleLogin } from '@react-oauth/google';
import axios from 'axios';

const GoogleLoginComponent = () => {
    const handleLoginSuccess = async (response) => {
        const { credential } = response;
        
        try {
            // Send the Google token to the backend for verification
            const res = await axios.post('http://localhost:5000/auth/google', {
                token: credential
            });
            console.log('Backend response:', res.data);
        } catch (error) {
            console.error('Login failed', error);
        }
    };

    const handleLoginFailure = (error) => {
        console.error('Login failed:', error);
    };

    return (
        <div className="login-container">
            <GoogleLogin 
                onSuccess={handleLoginSuccess}
                onError={handleLoginFailure}
                useOneTap
            />
        </div>
    );
};

export default GoogleLoginComponent;
