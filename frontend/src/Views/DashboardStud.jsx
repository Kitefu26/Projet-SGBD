import React from 'react';
import SidenavStud from '../Components/SidenavStud';
import Box from '@mui/material/Box';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Typography from '@mui/material/Typography';
import { Line } from 'react-chartjs-2';
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
} from 'chart.js';

// Enregistrement des composants de Chart.js
ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

// Exemple de données fictives
const rows = [
    { id: 1, subject: 'SGBD', title: 'Sujet CC', grade: 15 },
    { id: 2, subject: 'SGBD', title: 'Sujet DS', grade: 12 },
    { id: 3, subject: 'Programmation', title: 'Projet Final', grade: 18 },
];

// Préparation des données pour le graphique
const chartData = {
    labels: rows.map((row) => row.title), // Titres des sujets
    datasets: [
        {
            label: 'Notes',
            data: rows.map((row) => row.grade), // Notes des étudiants
            borderColor: 'rgba(75, 192, 192, 1)',
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            pointBackgroundColor: 'rgba(75, 192, 192, 1)',
            pointBorderColor: '#fff',
            pointBorderWidth: 2,
            pointRadius: 6,
            pointHoverRadius: 8,
            tension: 0.4,
        },
    ],
};

const chartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
        legend: {
            position: 'top',
            labels: {
                font: {
                    size: 14,
                },
            },
        },
        title: {
            display: true,
            text: 'Évolution des performances',
            font: {
                size: 18,
            },
        },
        tooltip: {
            callbacks: {
                label: (context) => `Note: ${context.raw}`,
            },
        },
    },
    scales: {
        x: {
            grid: {
                display: true,
                color: 'rgba(200, 200, 200, 0.2)',
            },
            ticks: {
                font: {
                    size: 12,
                },
            },
        },
        y: {
            grid: {
                display: true,
                color: 'rgba(200, 200, 200, 0.2)',
            },
            ticks: {
                font: {
                    size: 12,
                },
                stepSize: 5, // Ajuste l'intervalle des ticks
            },
            min: 0, // Définit la valeur minimale de l'axe Y
        },
    },
};

export default function DashboardStud() {
    return (
        <>
            <Box sx={{ display: 'flex' }}>
                <SidenavStud />
                <Box sx={{ flexGrow: 1, p: 3 }}>
                    {/* Tableau des notes */}
                    <Typography variant="h4" gutterBottom>
                        Tableau des notes
                    </Typography>
                    <TableContainer component={Paper} sx={{ mb: 4 }}>
                        <Table sx={{ minWidth: 650 }} aria-label="tableau des notes">
                            <TableHead>
                                <TableRow>
                                    <TableCell>Matière</TableCell>
                                    <TableCell>Titre</TableCell>
                                    <TableCell>Note</TableCell>
                                </TableRow>
                            </TableHead>
                            <TableBody>
                                {rows.map((row) => (
                                    <TableRow key={row.id}>
                                        <TableCell>{row.subject}</TableCell>
                                        <TableCell>{row.title}</TableCell>
                                        <TableCell>{row.grade}</TableCell>
                                    </TableRow>
                                ))}
                            </TableBody>
                        </Table>
                    </TableContainer>

                    {/* Graphique d'évolution des performances */}
                    <Typography variant="h4" gutterBottom>
                        Suivi des performances
                    </Typography>
                    <Paper elevation={3} sx={{ p: 3, height: '400px' }}>
                        <Line data={chartData} options={chartOptions} />
                    </Paper>
                </Box>
            </Box>
        </>
    );
}