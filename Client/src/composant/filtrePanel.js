// FiltrePanel.js
import React from "react";

const FilterPanel = ({
  selectedCategories,
  onCategoryChange,
  selectedLocation,
  onLocationChange,
  selectedMonth,
  onMonthChange,
}) => {
  return (
    <div style={{ marginBottom: "20px" }}>
      <label>Filtrer par catégorie : </label>
      <div>
        <label>
          <input
            type="checkbox"
            value="Emploi"
            checked={selectedCategories.includes("Emploi")}
            onChange={onCategoryChange}
          />
          Emploi / Travail
        </label>
      </div>

      <label style={{ marginLeft: "20px" }}>Filtrer par lieu : </label>
      <select value={selectedLocation} onChange={onLocationChange}>
        <option value="All">Tous</option>
        <option value="Paris">Paris</option>
        <option value="Lyon">Lyon</option>
        <option value="Marseille">Marseille</option>
        <option value="Bordeaux">Bordeaux</option>
      </select>

      <label style={{ marginLeft: "20px" }}>Filtrer par mois : </label>
      <input
        type="month"
        value={selectedMonth}
        onChange={onMonthChange}
      />
    </div>
  );
};

export default FilterPanel;
