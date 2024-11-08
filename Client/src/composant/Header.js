import React, { useState } from 'react'
import { Link } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBars } from '@fortawesome/free-solid-svg-icons';
import logo from '../image/LeHavreSeine.png';
import '../style/header.css';


export default function Header() {

    const [isOpen, setIsOpen] = useState(false);

    const toogleMenu = () => {
        setIsOpen(!isOpen);
    };

  return (
    <div class="header">
        <div class="header-logo">
            <img src={logo} alt="logo Le Havre Seine Métropole"/>
        </div>
        <div class="header-text">
            <p>CALENDRIER DES ÉVÈNEMENTS</p>
        </div>
        <div className={isOpen ? 'header-menu-open' : 'header-menu'}>
            {isOpen ? 
            <>
                <div>
                    <FontAwesomeIcon icon={faBars} size='2x' onClick={toogleMenu} className={isOpen ? 'rotate' : ''} />
                </div>       
                    <ul>
                        <li onClick={toogleMenu}><Link to="/">Accueil</Link></li>
                        <hr/>
                        <li onClick={toogleMenu}><Link to="/calendar">Calendrier</Link></li>
                        <hr/>
                        <li onClick={toogleMenu}><Link to="/events">Evénement</Link></li>
                    </ul>
            </>
            :
            <>
                <div onClick={toogleMenu}>
                    <FontAwesomeIcon icon={faBars} size='2x' />
                </div>
                <div onClick={toogleMenu}>
                    <p>MENU</p>
                </div>
            </>
            }
            
            

        </div>
    </div>
  )
}
