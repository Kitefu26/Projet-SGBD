import './App.css';
import DashboardProf from './Views/DashboardProf';
import AddExo from './Views/AddExo';
import DashboardAdmin from './Views/DashboardAdmin';
import {Routes, Route, BrowserRouter} from 'react-router-dom';
import DashboardStud from './Views/DashboardStud';
import AddModele from './Views/AddModele';
import ListerExoStud from './Views/ListExoStud';
import DeposerExercice from './Views/DepotExo';
import ListerExoProf from './Views/ListExoProf';

import { UserProvider } from './UserContext';

function App() {
    return (
        <UserProvider>
            <BrowserRouter>
                <Routes>
                    <Route path="/" exact element={<DashboardProf />} />
                    <Route path="/ajouter-exercice" exact element={<AddExo />} />
                    <Route path="/ajouter-modele" exact element={<AddModele />} />
                    <Route path="/dashboard-admin" exact element={<DashboardAdmin />} />
                    <Route path="/dashboard-student" exact element={<DashboardStud />} />
                    <Route path="/dashboard-prof" exact element={<DashboardProf />} />
                    <Route path="/lister-exercice-stud" exact element={<ListerExoStud />} />
                    <Route path="/deposer-exercice" exact element={<DeposerExercice />} />
                    <Route path="/lister-exercice" exact element={<ListerExoProf />} />
                </Routes>
            </BrowserRouter>
        </UserProvider>
    );
}

export default App;
