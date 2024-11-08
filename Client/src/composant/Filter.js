import React, { useState } from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faGraduationCap } from '@fortawesome/free-solid-svg-icons';

import '../style/filter.css'

export default function Filter() {
    const [evenementIsChecked, setEvenementIsChecked] = useState(false);
    const [formationIsChecked, setFormationIsChecked] = useState(false);
    const [selectedOption, setSelectedOption] = useState(1);

    const handleChange = (event) => {
        setSelectedOption(event.target.value);
    }

    const evenementChange = (event) => {
        setEvenementIsChecked(event.target.checked);
    };

    const formationChange = (event) => {
        setFormationIsChecked(event.target.checked)
    }

    const controlePeriode = ({ onViewChange }) => {

    }

  return (
    <div class="container">
        <div>
            <select value={selectedOption} onChange={handleChange}>
                <option value="1" >Mois</option>
                <option value="2" >Semaine</option>
                <option value="3" >Jours</option>
            </select>
        </div>
        <div>
            <label>
                <input 
                    type="checkbox"
                    checked={evenementIsChecked}
                    onChange={evenementChange}
                />
                Évènements
            </label>
        </div>
        <div>
            <label>
                <input 
                    type="checkbox"
                    checked={formationIsChecked}
                    onChange={formationChange}
                />
                <FontAwesomeIcon icon={faGraduationCap} size='lg' />
                Emploi/formation
            </label>
        </div>
    </div>
  )
}
