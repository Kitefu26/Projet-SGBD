import * as React from 'react';
import Box from '@mui/material/Box';
import Drawer from '@mui/material/Drawer';
import CssBaseline from '@mui/material/CssBaseline';
import Toolbar from '@mui/material/Toolbar';
import List from '@mui/material/List';
import Typography from '@mui/material/Typography';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemText from '@mui/material/ListItemText';
import Topbar from './Topbar'; // Importer le composant Topbar

import { useNavigate } from 'react-router-dom';

const drawerWidth = 240;

export default function Sidenav() {
  const navigate = useNavigate();

  return (
    <Box sx={{ display: 'flex' }}>
      <CssBaseline />
      <Topbar /> {/* Ajouter le composant Topbar */}
      <Drawer
        sx={{
          width: drawerWidth,
          flexShrink: 0,
          '& .MuiDrawer-paper': {
            width: drawerWidth,
            boxSizing: 'border-box',
            backgroundColor: '#000', // Fond noir pour le Drawer
            color: '#fff', // Texte en blanc
          },
        }}
        variant="permanent"
        anchor="left"
      >
        <Toolbar />
        <List dense>
          <ListItem disablePadding sx={{ display: 'block' }} onClick={() => navigate('/dashboard-student')}>
            <ListItemButton
              sx={{
                border: '1px solid #d1d9e6', // Contour gris clair
                borderRadius: '6px', // Coins légèrement arrondis
                marginBottom: '6px', // Espacement réduit entre les boutons
                '&:hover': {
                  backgroundColor: '#333', // Couleur de fond douce au survol
                },
              }}
            >
              <ListItemText
                primary="Accueil"
                sx={{
                  fontFamily: 'Arial, sans-serif', // Police personnalisée
                  fontWeight: 'bold', // Texte en gras
                  fontSize: '20px', // Taille de la police
                  color: '#fff', // Couleur du texte en blanc
                }}
              />
            </ListItemButton>
          </ListItem>
          <ListItem disablePadding sx={{ display: 'block' }} onClick={() => navigate('/lister-exercice-stud')}>
            <ListItemButton
              sx={{
                border: '1px solid #d1d9e6',
                borderRadius: '6px',
                marginBottom: '6px',
                '&:hover': {
                  backgroundColor: '#333',
                },
              }}
            >
              <ListItemText
                primary="Lister les exercices"
                sx={{
                  fontFamily: 'Arial, sans-serif',
                  fontWeight: 'bold',
                  fontSize: '20px',
                  color: '#fff',
                }}
              />
            </ListItemButton>
          </ListItem>
        </List>
      </Drawer>
      <Box
        component="main"
        sx={{ flexGrow: 1, bgcolor: 'background.default', p: 3 }}
      >
        <Toolbar />
        <Typography sx={{ marginBottom: 2 }}>
        </Typography>
      </Box>
    </Box>
  );
}
