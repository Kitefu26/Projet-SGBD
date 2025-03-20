import React, { useState } from 'react';
import SidenavStud from '../Components/SidenavStud';
import Box from '@mui/material/Box';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import { useNavigate } from 'react-router-dom';

export default function ListExoStud() {
    const navigate = useNavigate();
    const [rows, setRows] = useState([]);

    // Fonction pour gérer la validation d'un fichier
    const handleValidateFile = (id) => {
        setRows((prevRows) =>
            prevRows.map((row) =>
                row.id === id ? { ...row, fileSubmitted: true } : row
            )
        );
    };

    return (
        <>
            <Box sx={{ display: 'flex' }}>
                <SidenavStud />
                <Box sx={{ flexGrow: 1, p: 3 }}>
                    <h1>Liste des exercices</h1>
                    <TableContainer component={Paper}>
                        <Table sx={{ minWidth: 650 }} aria-label="tableau des exercices">
                            <TableHead>
                                <TableRow>
                                    <TableCell>Titre</TableCell>
                                    <TableCell>Matière</TableCell>
                                    <TableCell>Date limite</TableCell>
                                    <TableCell>Action</TableCell>
                                </TableRow>
                            </TableHead>
                            <TableBody>
                                {rows.length === 0 ? (
                                    <TableRow>
                                        <TableCell colSpan={4} align="center">
                                            Aucun exercice disponible
                                        </TableCell>
                                    </TableRow>
                                ) : (
                                    rows.map((row) => (
                                        <TableRow key={row.id}>
                                            <TableCell>{row.title}</TableCell>
                                            <TableCell>{row.subject}</TableCell>
                                            <TableCell>{row.deadline}</TableCell>
                                            <TableCell>
                                                {!row.fileSubmitted ? (
                                                    <>
                                                        <Button
                                                            variant="contained"
                                                            color="primary"
                                                            onClick={() => navigate('/deposer-exercice', {
                                                                state: { id: row.id, title: row.title }
                                                            })}
                                                        >
                                                            Déposer
                                                        </Button>
                                                        <Button
                                                            variant="contained"
                                                            color="secondary"
                                                            onClick={() => handleValidateFile(row.id)}
                                                            sx={{ ml: 2 }}
                                                        >
                                                            Valider
                                                        </Button>
                                                    </>
                                                ) : (
                                                    <Typography color="textSecondary">
                                                        Déjà déposé
                                                    </Typography>
                                                )}
                                            </TableCell>
                                        </TableRow>
                                    ))
                                )}
                            </TableBody>
                        </Table>
                    </TableContainer>
                </Box>
            </Box>
        </>
    );
}