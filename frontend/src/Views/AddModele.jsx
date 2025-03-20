import React, { useState, useCallback } from 'react';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Paper from '@mui/material/Paper';
import Typography from '@mui/material/Typography';
import { useDropzone } from 'react-dropzone';
import Sidenav from '../Components/sidenav';

export default function AddModele() {
    // État pour stocker les fichiers sélectionnés
    const [files, setFiles] = useState([]);

    // Fonction appelée quand des fichiers sont déposés dans la zone de drop
    const onDrop = useCallback((acceptedFiles) => {
        setFiles((prevFiles) => [...prevFiles, ...acceptedFiles]);
    }, []);

    // Configuration de react-dropzone
    const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop });

    // Gestion de la sélection de fichiers via le bouton
    const handleFileInputChange = (event) => {
        const newFiles = Array.from(event.target.files);
        setFiles((prevFiles) => [...prevFiles, ...newFiles]);
    };

    return (
        <>
            <Box sx={{ display: 'flex' }}>
                <Sidenav />
                <Box sx={{ flexGrow: 1, p: 3 }}>
                    {/* Titre de la page */}
                    <Typography variant="h4" gutterBottom>
                        Ajouter modèle
                    </Typography>

                    {/* Zone de drag and drop */}
                    <Paper elevation={10} sx={{ p: 3, mb: 3, borderRadius: '25px' }}>
                        <div
                            {...getRootProps()}
                            style={{
                                border: '2px dashed #ccc',
                                borderRadius: '20px',
                                paddingBottom: '150px',
                                paddingTop: '150px',
                                paddingLeft: '50px',
                                paddingRight: '50px',
                                textAlign: 'center',
                            }}
                        >
                            <input {...getInputProps()} />
                            {isDragActive ? (
                                <Typography>Déposez les fichiers ici...</Typography>
                            ) : (
                                <Typography>
                                    Glissez et déposez des fichiers ici, ou cliquez pour sélectionner des fichiers
                                </Typography>
                            )}
                             {/* Bouton pour importer depuis les dossiers */}
                            <input
                                type="file"
                                multiple
                                onChange={handleFileInputChange}
                                style={{ display: 'none' }}
                                id="file-input"
                            />
                            <label htmlFor="file-input">
                                <Button variant="contained" component="span">
                                    Importer
                                </Button>
                            </label>
                        </div>
                    </Paper>

                    {/* Liste des fichiers sélectionnés */}
                    {files.length > 0 && (
                        <Box sx={{ mt: 3 }}>
                            <Typography variant="h6">Fichiers sélectionnés :</Typography>
                            <ul>
                                {files.map((file, index) => (
                                    <li key={index}>{file.name}</li>
                                ))}
                            </ul>
                        </Box>
                    )}
                </Box>
            </Box>
        </>
    );
}