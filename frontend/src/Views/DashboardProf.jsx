import React, { useState } from 'react';
import Sidenav from '../Components/sidenav';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import { DataGrid } from '@mui/x-data-grid';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

export default function DashboardProf() {
    // Liste des étudiants avec des notes entre 0 et 20
    const [rows, setRows] = useState([
        { id: 1, name: 'John Doe', grade: 15, grade2: 14, email: 'john@gmail.com'},
        { id: 2, name: 'Jane Smith', grade: 18, grade2: 17, email: 'jane@gamil.com' },
        { id: 3, name: 'Alice Johnson', grade: 12, grade2: 13, email: 'alice@gmail.com' },
        { id: 4, name: 'Bob Brown', grade: 9, grade2: 10, email: 'bob@gmail.com'},
        { id: 5, name: 'Charlie Davis', grade: 20, grade2: 19, email: 'charlie@gmail.com' },
        { id: 6, name: 'Diana Evans', grade: 14, grade2: 15, email: 'diana@gmail.com' },
        { id: 7, name: 'Ethan Foster', grade: 7, grade2: 8, email: 'ethan@gmail.com' },
        { id: 8, name: 'Fiona Green', grade: 11, grade2: 12, email: 'fiona@gmail.com' },
        { id: 9, name: 'George Harris', grade: 16, grade2: 15, email: 'george@gmail.com' },
        { id: 10, name: 'Hannah White', grade: 19, grade2: 18, email: 'hannah@gmail.com' },
        { id: 11, name: 'Isaac Young', grade: 13, grade2: 14, email: 'isaac@gmail.com' },
        { id: 12, name: 'Jack Black', grade: 10, grade2: 11, email: 'jack@gmail.com' },
        { id: 13, name: 'Katie Brown', grade: 8, grade2: 9, email: 'katie@gmail.com' },
        { id: 14, name: 'Liam Smith', grade: 17, grade2: 16, email: 'liam@gmail.com' }
    ]);

    const columns = [
        { field: 'id', headerName: 'ID', width: 100 },
        { field: 'name', headerName: 'Nom', width: 200 },
        { 
            field: 'grade', 
            headerName: 'Note 1', 
            width: 150, 
            editable: true // Permet l'édition de la colonne "Note 1"
        },
        { 
            field: 'grade2', 
            headerName: 'Note 2', 
            width: 150, 
            editable: true // Permet l'édition de la colonne "Note 2"
        },
        { field: 'email', headerName: 'Email', width: 300 }
    ];

    // Gestionnaire pour mettre à jour les données après modification
    const handleProcessRowUpdate = (newRow) => {
        const updatedRows = rows.map((row) => (row.id === newRow.id ? newRow : row));
        setRows(updatedRows);
        return newRow;
    };

    // Calcul des données pour le graphique
    const chartData = rows.map((row) => ({
        name: row.name,
        moyenne: (row.grade + row.grade2) / 2, // Moyenne des deux notes
        grade: row.grade,
        grade2: row.grade2
    }));

    return (
        <>
            <Box sx={{ display: 'flex' }}>
                <Sidenav />
                <Box sx={{ flexGrow: 1, p: 3 }}>
                    <h1>Dashboard</h1>
                    <Paper sx={{ height: 400, width: '100%', marginBottom: 3 }}>
                        <h3>Liste des étudiants</h3>
                        <DataGrid
                            rows={rows}
                            columns={columns}
                            pageSize={10} // Limite l'affichage à 10 lignes par page
                            pageSizeOptions={[10]} // Options de pagination (uniquement 10 ici)
                            checkboxSelection
                            sx={{ border: 0 }}
                            processRowUpdate={handleProcessRowUpdate} // Gestion des modifications
                            experimentalFeatures={{ newEditingApi: true }} // Active l'API d'édition
                        />
                    </Paper>
                    <Paper sx={{ height: 400, width: '100%' }}>
                        <h3>Évolution des notes des étudiants</h3>
                        <ResponsiveContainer width="100%" height="100%">
                            <LineChart data={chartData}>
                                <CartesianGrid strokeDasharray="3 3" />
                                <XAxis dataKey="name" />
                                <YAxis />
                                <Tooltip />
                                <Legend />
                                {/* Ligne pour la première note */}
                                <Line type="monotone" dataKey="grade" stroke="#8884d8" name="Note 1" activeDot={{ r: 8 }} />
                                {/* Ligne pour la deuxième note */}
                                <Line type="monotone" dataKey="grade2" stroke="#82ca9d" name="Note 2" activeDot={{ r: 8 }} />
                            </LineChart>
                        </ResponsiveContainer>
                    </Paper>
                </Box>
            </Box>
        </>
    );
}