import React, { useCallback, useEffect, useState } from "react";
import { useDropzone } from "react-dropzone";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import Paper from "@mui/material/Paper";
import Typography from "@mui/material/Typography";
import TextField from "@mui/material/TextField";
import CircularProgress from "@mui/material/CircularProgress";
import Snackbar from "@mui/material/Snackbar";
import MuiAlert from "@mui/material/Alert";
import Sidenav from "../Components/sidenav";
import { useUser } from "../UserContext"; // Ensure this is the correct path
export default function AddExo() {
    const [files, setFiles] = useState([]);
    const [titre, setTitre] = useState("");
    const [description, setDescription] = useState("");
    const [dateDepot, setDateDepot] = useState("");
    const [professeur, setProfesseur] = useState("");
    const user = useUser();

    useEffect(() => {
        if (user) {
            setProfesseur(user.id); // Assuming user object has an id field
        }
    }, [user]);

    const [uploading, setUploading] = useState(false);
    const [message, setMessage] = useState("");
    const [openSnackbar, setOpenSnackbar] = useState(false);
    const [, setExercices] = useState([]);

    useEffect(() => {
        fetch("http://127.0.0.1:8000/api/exercices/")
            .then((response) => response.json())
            .then((data) => setExercices(data))
            .catch((error) => console.error("Erreur de récupération des exercices :", error));
    }, []);

    const onDrop = useCallback((acceptedFiles) => {
        setFiles((prevFiles) => [...prevFiles, ...acceptedFiles]);
    }, []);

    const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop });

    const handleFileInputChange = (event) => {
        const newFiles = Array.from(event.target.files);
        setFiles((prevFiles) => [...prevFiles, ...newFiles]);
    };

    const removeFile = (index) => {
        setFiles(files.filter((_, i) => i !== index));
    };

    const handleCloseSnackbar = () => {
        setOpenSnackbar(false);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        setMessage("");
        setUploading(true);

        if (!titre || !description || !dateDepot || files.length === 0) {
            setMessage("Veuillez remplir tous les champs et ajouter au moins un fichier.");
            setOpenSnackbar(true);
            setUploading(false);
            return;
        }

        const formData = new FormData();
        formData.append("titre", titre);
        formData.append("description", description);
        formData.append("date_depot", dateDepot);
        formData.append("professeur", professeur);
        files.forEach((file) => formData.append("fichier", file));

        try {
            const response = await fetch("http://127.0.0.1:8000/api/exercices/", {
                method: "POST",
                body: formData,
            });

            if (response.ok) {
                setMessage("Exercice ajouté avec succès !");
                setTitre("");
                setDescription("");
                setDateDepot("");
                setFiles([]);
                fetch("http://127.0.0.1:8000/api/exercices/")
                    .then((res) => res.json())
                    .then((data) => setExercices(data));
            } else {
                setMessage("Erreur lors de l'ajout de l'exercice.");
            }
        } catch (error) {
            setMessage("Erreur de connexion au serveur.");
        } finally {
            setOpenSnackbar(true);
            setUploading(false);
        }
    };

    return (
        <>
            <Box sx={{ display: "flex" }}>
                <Sidenav />
                <Box sx={{ flexGrow: 1, p: 3 }}>
                    <Typography variant="h4" gutterBottom>
                        Ajouter un exercice
                    </Typography>

                    <Paper elevation={10} sx={{ p: 3, mb: 3, borderRadius: "25px" }}>
                        <form onSubmit={handleSubmit}>
                            <TextField
                                label="Titre de l'exercice"
                                fullWidth
                                margin="normal"
                                value={titre}
                                onChange={(e) => setTitre(e.target.value)}
                            />
                            <TextField
                                label="Description"
                                fullWidth
                                multiline
                                rows={4}
                                margin="normal"
                                value={description}
                                onChange={(e) => setDescription(e.target.value)}
                            />
                            <TextField
                                label="Date de dépôt"
                                type="datetime-local"
                                fullWidth
                                margin="normal"
                                InputLabelProps={{ shrink: true }}
                                value={dateDepot}
                                onChange={(e) => setDateDepot(e.target.value)}
                            />

                            <div
                                {...getRootProps()}
                                style={{
                                    border: "2px dashed #ccc",
                                    borderRadius: "20px",
                                    padding: "20px",
                                    textAlign: "center",
                                    cursor: "pointer",
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
                            </div>

                            <input
                                type="file"
                                multiple
                                onChange={handleFileInputChange}
                                style={{ display: "none" }}
                                id="file-input"
                            />
                            <label htmlFor="file-input">
                                <Button variant="contained" component="span" sx={{ mt: 2 }}>
                                    Importer
                                </Button>
                            </label>

                            {files.length > 0 && (
                                <Box sx={{ mt: 3 }}>
                                    <Typography variant="h6">Fichiers sélectionnés :</Typography>
                                    <ul>
                                        {files.map((file, index) => (
                                            <li key={index}>
                                                {file.name}
                                                <Button size="small" color="error" onClick={() => removeFile(index)}>
                                                    Supprimer
                                                </Button>
                                            </li>
                                        ))}
                                    </ul>
                                </Box>
                            )}

                            {uploading && <CircularProgress sx={{ display: "block", mt: 2 }} />}

                            <Button type="submit" variant="contained" color="primary" sx={{ mt: 3 }}>
                                Ajouter l'exercice
                            </Button>
                        </form>
                    </Paper>

                    <Snackbar open={openSnackbar} autoHideDuration={4000} onClose={handleCloseSnackbar}>
                        <MuiAlert onClose={handleCloseSnackbar} severity="info" sx={{ width: "100%" }}>
                            {message}
                        </MuiAlert>
                    </Snackbar>
                </Box>
            </Box>
        </>
    );
}