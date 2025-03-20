import React, { useCallback, useState } from 'react';
import { useDropzone } from 'react-dropzone';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Paper from '@mui/material/Paper';
import Typography from '@mui/material/Typography';
import Sidenav from '../Components/SidenavStud';
import { useNavigate } from 'react-router-dom';

export default function DepotExo() {
    // État pour stocker le fichier sélectionné
    const [file, setFile] = useState(null);

    // Initialisation de la navigation
    const navigate = useNavigate();

    // Fonction appelée quand un fichier est déposé dans la zone de drop
    const onDrop = useCallback((acceptedFiles) => {
        if (acceptedFiles.length > 0) {
            setFile(acceptedFiles[0]); // Remplace le fichier existant
        }
    }, []);

    // Configuration de react-dropzone
    const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop, multiple: false });

    // Gestion de la sélection de fichier via le bouton
    const handleFileInputChange = (event) => {
        if (event.target.files.length > 0) {
            setFile(event.target.files[0]); // Remplace le fichier existant
        }
    };

    return (
        <>
            <Box sx={{ display: 'flex' }}>
                <Sidenav />
                <Box sx={{ flexGrow: 1, p: 3 }}>
                    {/* Titre de la page */}
                    <Typography variant="h4" gutterBottom>
                        Déposer exercice
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
                                <Typography>Déposez le fichier ici...</Typography>
                            ) : (
                                <Typography>
                                    Glissez et déposez un fichier ici, ou cliquez pour sélectionner un fichier
                                </Typography>
                            )}
                            {/* Bouton pour importer depuis les dossiers */}
                            <input
                                type="file"
                                accept="application/pdf"
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

                    {/* Affichage du fichier sélectionné */}
                    {file && (
                        <Box sx={{ mt: 3 }}>
                            <Typography variant="h6">Fichier sélectionné :</Typography>
                            <ul>
                                <li>{file.name}</li>
                            </ul>

                            {/* Affichage du PDF */}
                            {file.type === 'application/pdf' && (
                                <Box sx={{ mt: 3, mb: 3 }}>
                                    <Typography variant="h6">Aperçu du fichier :</Typography>
                                    <iframe
                                        src={URL.createObjectURL(file)}
                                        title="Aperçu PDF"
                                        width="100%"
                                        height="500px"
                                        style={{ border: '1px solid #ccc', borderRadius: '10px' }}
                                    ></iframe>
                                </Box>
                            )}

                            {/* Bouton Valider */}
                            <Button
                                variant="contained"
                                color="primary"
                                onClick={() => navigate('/lister-exercice-stud')}
                                sx={{ mt: 2 }}
                            >
                                Valider
                            </Button>
                        </Box>
                    )}
                </Box>
            </Box>
        </>
    );
}