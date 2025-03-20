import React from 'react';
import Sidenav from '../Components/sidenav';
import Box from '@mui/material/Box';

export default function DashboardAdmin() {
    return (
        <>
        <Box sx={{ display: 'flex' }}>
            <Sidenav />
            <h1>Dashboard</h1>
        </Box>
        </>
    );
}