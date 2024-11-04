import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBars } from '@fortawesome/free-solid-svg-icons';
import logo from '../image/LeHavreSeine.png';
import burger from '../image/menu.png';
import '../style/header.css';


export default function Header() {
  return (
    <div class="header">
        <div class="header-logo">
            <img src={logo} alt="logo Le Havre Seine Métropole"/>
        </div>
        <div class="header-text">
            <p>CALENDRIER DES ÉVÈNEMENTS</p>
        </div>
        <div class="header-menu">
            <div>
                <FontAwesomeIcon icon={faBars} size='2x' />
            </div>
            <div>
                <p>MENU</p>
            </div>
        </div>
    </div>
  )
}
