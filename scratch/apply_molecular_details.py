import json
import os

def update_06_abilities():
    fpath = 'Kara No/06_Abilities.json'
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Entry 1: MEoDP
    meodp_mol = """

[MOLECULAR & SOMATIC BIOPHYSICS OF MEoDP]
- Neuro-Ocular Pathway to Akasha:
  * Optical Processing vs. Metaphysical Routing: Conventional human vision begins with photonic excitation of rhodopsin and photopsin in retinal rods and cones, transmitting graded potentials through bipolar cells to retinal ganglion cells, whose axons form the optic nerve (cranial nerve II). Signals traverse the optic chiasm, synapse in the Lateral Geniculate Nucleus (LGN) of the thalamus, and project via optic radiations to the primary visual cortex (Brodmann Area 17 / V1).
  * The Direct Conduit: In Ryougi Shiki, MEoDP operates by directly interfacing this neural visual processing matrix with the Swirl of the Root (Akasha). The perception of death bypasses ocular retinal transduction entirely—she can see the lines and points of death even in pitch-black darkness, through blindfolds, or with her physical eyelids closed, because the visual cortex receives structural entropy data rendered directly into her consciousness.
- Molecular Disintegration vs. Mechanical Bond Cleavage:
  * In classical physics and chemistry, cutting a material requires mechanical work to overcome the Lennard-Jones intermolecular potentials and covalent bond dissociation energy (e.g., ~348 kJ/mol for C-C single bonds, ~413 kJ/mol for C-H bonds). This mechanical cleavage generates frictional heat, shear stress, and acoustic pressure waves.
  * Tracing a Line of Death requires strictly zero physical force (Work = 0 Joules). It does not break chemical bonds through mechanical shear; rather, it executes an ontological nullification of the object's existential coordinate within Akasha. At the exact coordinate traversed by the blade, the conceptual identity holding the atoms together is erased. Consequently, covalent, ionic, and hydrogen bonds instantly dissolve, and the macroscopic material splits along a mirror-smooth molecular plane without resistance, thermal dissipation, or structural deformation.
- Thermodynamic Heat Dissipation & Brain Strain Paradox:
  * Why Ryougi Suffers Zero Neural Burnout: Ryougi Shiki's physical body and soul origin is 「　」 (Void / Nothingness). Her brain acts as a zero-impedance superconducting conduit to Akasha. There is zero resistance to the metaphysical data flow; hence, her cerebral micro-vessels, glial cells, and neuronal myelin sheaths remain at baseline body temperature (37°C) without micro-hemorrhaging or cerebral edema.
  * Contrast with Tohno Shiki: Tohno lacks a direct Origin-connection to the Root; his ordinary human biological hardware is forced to decode non-Euclidean mortality concepts through finite biological neurons. This induces massive metabolic hyperthermia, overtaxes sodium-potassium pumps (Na+/K+ ATPase), and causes micro-aneurysms, excruciating migraines, and permanent cortical necrosis.
- Conceptual Severing of Microscopic Pathogens:
  * In Chapter 3 (Remaining Sense of Pain), Shiki stabs Fujino's lower right abdomen to sever the mortality of her acute appendicitis. Shiki perceived the death lines belonging specifically to the bacterial infection (Escherichia coli and anaerobic Bacteroides fragilis colonization) and the gangrenous necrosis of the vermiform appendix tissue.
  * The incision severed the existential persistence of the disease itself while preserving the surrounding visceral peritoneum, mesenteric blood vessels, and adjacent healthy ileocecal junction."""

    if "[MOLECULAR & SOMATIC BIOPHYSICS OF MEoDP]" not in data['entries']['1']['content']:
        data['entries']['1']['content'] += meodp_mol

    # Entry 2: Distortion
    dist_mol = """

[MOLECULAR SHEAR DYNAMICS & CRYSTALLINE FAILURE]
- Non-Euclidean Metric Tensor Warping:
  * Asagami Fujino's Mystic Eyes of Distortion do not generate kinetic force fields or telekinetic mass. Instead, they project localized spatial curvature directly into the Minkowski spacetime metric (g_mu_nu).
  * Dual-Axis Torsional Field: Fujino designates a central spatial axis within her perceptual field. Her left eye applies positive clockwise torsion while her right eye exerts negative counter-clockwise torsion. The resulting spatial gradient produces an instantaneous differential shear strain at the boundary interface.
- Crystalline Lattice Dislocation & Structural Steel Rupture:
  * When applied to inorganic structural materials—such as the high-tensile structural steel (SS400 / SM490) and reinforced concrete pillars of the Broad Bridge—the metric torsion induces instantaneous dislocation cascades along crystallographic slip planes within the iron-carbon crystalline lattice.
  * Because the physical space itself is twisting, the internal shear stress instantly exceeds the ultimate shear strength (tau_max >> 500 MPa) across every cubic micrometer of the cross-section simultaneously. The steel does not melt or bend smoothly; it undergoes catastrophic intergranular cleavage fracture, shearing thick steel girders as effortlessly as twisting dry noodles.
- Visceral & Cellular Membrane Disruption in Organic Tissue:
  * In biological organisms (e.g., Fujino's attackers in Chapter 3), the counter-rotational metric distortion exerts extreme torsional tension on organic micro-structures.
  * The phospholipid bilayers of cellular membranes are torn apart by localized shearing forces, causing massive intracellular fluid leakage. Capillary endothelial walls rupture instantaneously under hydrostatic pressure differentials, while collagen fibrils in skin, ligaments, and skeletal muscle bundles are twisted into helical ropes before snapping. The victim's limbs and torso are wrung out like a soaked towel, expelling internal fluids along microscopic tissue fissures.
- Clairvoyance & Isometric Metric Warping:
  * Upon awakening Clairvoyance (千里眼) during the duel on the Broad Bridge, Fujino's perceptual coordinate system transitioned from focal retinotopic vision to an omnidirectional satellite spatial map.
  * She was no longer constrained by the optical horizon of her fovea centralis. By mapping the three-dimensional geometric coordinates of the entire suspension bridge in her mind, she could project metric torsion tensors onto structural support cables and underwater pilings hidden completely from direct sight."""

    if "[MOLECULAR SHEAR DYNAMICS & CRYSTALLINE FAILURE]" not in data['entries']['2']['content']:
        data['entries']['2']['content'] += dist_mol

    # Entry 6: Puppets
    puppet_mol = """

[SYNTHETIC CYTOLOGY & BIO-THAUMATURGICAL REPLICATION]
- Cellular Synthesis & Genetic Integrity:
  * Aozaki Touko's masterwork puppets are not constructed from inanimate wax, wood, or ceramic; they are genuine biological replicas synthesized down to the molecular and genetic level.
  * De Novo Genome Replication: Using alchemically distilled organic substrates and synthetic polymerase analogues, Touko synthesizes an identical 3-billion-base-pair human genome matching her own chromosomes. Her puppets possess fully functional cellular organelles: phospholipid bilayer membranes, ribosomal protein synthesis machinery, and metabolic mitochondria.
  * Mitotic Viability & Hematopoiesis: The puppet bodies possess living, vascularized bone marrow capable of authentic hematopoiesis—producing live erythrocytes (red blood cells), leukocytes (white blood cells), and thrombocytes (platelets) with matching Rh+ blood groups. The tissues undergo standard cellular respiration, consuming glucose and oxygen while producing ATP.
- Bio-Synthetic Magic Circuit Integration:
  * The puppet's Magic Circuits are not metallic wires or foreign conduits; they are bio-thaumaturgical nerve bundles woven directly along peripheral axon tracts and wrapped within synthetic myelin sheaths.
  * Prana Conduction & Od Storage: The circuits exhibit zero electrical or thaumaturgical impedance mismatch compared to Touko's original biological nervous system, allowing seamless Od generation and structural reinforcement."""

    if "[SYNTHETIC CYTOLOGY & BIO-THAUMATURGICAL REPLICATION]" not in data['entries']['6']['content']:
        data['entries']['6']['content'] += puppet_mol

    # Entry 7: Touko Techniques
    touko_tech_mol = """

[QUANTUM-THAUMATURGICAL SOUL TRANSIT & IDENTITY CONTINUUM]
- Zero-Delay Transmigration Upon Brain Death:
  * Touko's Grand-tier puppetry operates on the metaphysical Law of Indistinguishability. In classical thaumaturgy, a soul leaving a dead vessel disperses toward the Swirl of the Root because it recognizes the loss of its unique physical container.
  * Touko circumvents this dissolution: each cold-storage puppet body in her concealed workshops is an exact molecular, cellular, and neurological duplicate of her current physical self, down to the synaptome and memory engrams.
  * When Touko suffers fatal trauma (e.g., decapitation by Cornelius Alba or crushing by Araya Souren), the cessation of electrical synaptic activity in the dying brain acts as a quantum trigger. The soul (animus) does not enter Akasha; it instantly instantiates within the nearest ready duplicate. Because the incoming container is 100% physically and neurologically identical, the soul experiences zero transitional entropy, and Touko awakens seamlessly, lighting a fresh cigarette without a gap in subjective consciousness.
- Norse Rune Plasma Kinetics (Ansuz):
  * Touko's primary offensive and utilitarian magecraft utilizes the ancient Elder Futhark rune Ansuz (ᚫ - Breath of the God / Flame).
  * Rather than invoking external spirits, the rune trace acts as an electrical and thaumaturgical potential gradient that strips electrons from ambient atmospheric diatomic nitrogen (N2) and oxygen (O2), generating a pocket of non-equilibrium thermal plasma. The resulting heat pulse instantly ignites tobacco hydrocarbons in under 15 milliseconds without requiring match friction or flint strikes."""

    if "[QUANTUM-THAUMATURGICAL SOUL TRANSIT & IDENTITY CONTINUUM]" not in data['entries']['7']['content']:
        data['entries']['7']['content'] += touko_tech_mol

    # Entry 10: Araya Techniques
    araya_tech_mol = """

[ŚARĪRA DIAMOND-LATTICE OSSIFICATION & SPATIAL COMPRESSION]
- Crystalline Transmutation of Bone Structure:
  * The three holy Śarīra relics (Buddha's bone fragments) surgically grafted into Araya Souren's left ulna, radius, and thoracic cage have completely transfigured his biological skeletal tissue over 200 years of meditative assimilation.
  * Microscopic Lattice Density: The biological calcium hydroxyapatite (Ca10(PO4)6(OH)2) in his bones has been replaced by a crystalline diamond-cubic vajra-mineral matrix. This biological crystallization yields a structural hardness exceeding Mohs scale 10, rendering his skeletal frame impervious to high-caliber kinetic munitions, hydraulic crushing, and conventional molecular oxidation.
  * Cellular Stasis: The divine sanctity of the Śarīra halts cellular senescence entirely. His telomeres do not shorten; his somatic cells remain locked in permanent metabolic homeostasis.
- Spatial Metric Contraction (六道境界 / Rokudou Kyoukai):
  * When Araya activates his personal Bounded Field, he does not merely push air or erect an invisible wall; he compresses the spatial metric volume within a designated radius around his torso.
  * Projectile Kinetic Dissipation: When Shiki's knife or physical attacks enter this boundary, the physical distance they must traverse increases exponentially despite the macroscopic appearance of a few centimeters. The projectile's kinetic energy (Ek = 1/2 mv^2) is drained as work performed against the expanding spatial metric tension, causing blades and bullets to slow to a complete standstill in mid-air."""

    if "[ŚARĪRA DIAMOND-LATTICE OSSIFICATION & SPATIAL COMPRESSION]" not in data['entries']['10']['content']:
        data['entries']['10']['content'] += araya_tech_mol

    # Entry 11: Prosthetic Arm
    arm_mol = """

[BIOMECHANICAL POLYMERS & HYDRAULIC FORCE TRANSFERS]
- Micro-Structural Composition:
  * Structural Shell: High-density synthetic ivory resin cross-linked with carbonized yew core fibers, providing immense compressive strength while maintaining an external surface that matches human epidermal texture and body warmth.
  * Artificial Myofibrils & Galvanic Actuation: Embedded within the forearm are bundles of electro-active synthetic muscle polymers (polyacrylonitrile myofibril analogues). These contract and expand in response to micro-voltage action potentials emitted by the surviving motor axon stumps in Shiki's left brachial plexus.
- Pseudo-Hemoglobin Spirit Conduction Fluid:
  * The internal hydraulic system is charged with an alchemically distilled organo-metallic fluid. This fluid replicates the viscosity, density, and thermal capacity of whole human blood while functioning as a high-permeability thaumaturgical conduit for Shiki's Od.
  * Crushing Force Dynamics: When hydraulic valves lock under thaumaturgical command, the prosthetic fingers can generate over 12,000 Newtons of mechanical force (~1.2 metric tons of pressure), sufficient to shatter structural granite or crush human cervical vertebrae to powder.
- Ectoplasmic Phase-Grounding & Spectral Manipulation:
  * Incorporeal entities (ghosts, wraiths, astral projections) exist as coherent configurations of spiritual ether, lacking baryonic mass and passing freely through standard atomic lattices.
  * The prosthetic arm's alchemical ivory coating is treated with a thaumaturgical grounding reagent. When the limb makes contact with an astral body, it projects an inverted polarity field that momentarily forces the ether into localized phase-density. This gives the ghost an artificial physical boundary, enabling Shiki to grip, lift, and pin incorporeal spirits with her prosthetic hand as though they possessed solid human flesh.
- Precision Elbow Decoupling:
  * A spring-loaded titanium-alloy ball-detent release mechanism is situated at the cubital joint. By performing an intentional, localized micro-twitch of her triceps brachii tendon, Shiki can release the locking pin in under 30 milliseconds, allowing the arm to cleanly disconnect while an enemy's weapon is embedded within it."""

    if "[BIOMECHANICAL POLYMERS & HYDRAULIC FORCE TRANSFERS]" not in data['entries']['11']['content']:
        data['entries']['11']['content'] += arm_mol

    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("06_Abilities.json updated successfully!")

def update_01_shiki():
    fpath = 'Kara No/01_Shiki.json'
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Entry 0: Ryougi Shiki
    shiki_kenjutsu_mol = """

[SOMATIC & NEUROLOGICAL KORYŪ KENJUTSU RECONFIGURATION]
- Classical Edo Swordsmanship Somatic Transformation:
  * When Shiki relinquishes her street knife and grips the two-handed tsuka of the Kujikane Kanesada katana, her body undergoes an instantaneous, involuntary somatic and neurological reconfiguration rooted in centuries of Ryougi clan ancestral conditioning.
  * Autonomic Vascular Shunting: Her sympathetic nervous system triggers selective peripheral vasoconstriction in non-essential mesenteric and splanchnic vascular beds, rerouting roughly 40% of systemic cardiac output directly to high-velocity skeletal muscle groups—specifically the latissimus dorsi, rhomboids, gluteal muscles, and quadriceps femoris.
  * Cellular Anaerobic Glide & Respiration Suspension: Her pulmonary respiration halts; thoracic wall movements and diaphragmatic contractions cease entirely. Shiki's muscle fibers transition into a hyper-efficient anaerobic metabolic glide, completely eliminating the 10-15 Hz involuntary physiological tremor and respiratory chest movements that normally degrade the precision of human blade trajectories.
  * Kinetic Torque & Skeletal Alignment: Her strikes do not rely on muscular straining; she aligns the radius, ulna, and humerus into rigid geometric lever arms that transmit rotational torque directly from hip torsion (pelvic rotation) through the spine, producing lethal cutting velocity with near-zero aerodynamic turbulence or audible blade friction."""

    if "[SOMATIC & NEUROLOGICAL KORYŪ KENJUTSU RECONFIGURATION]" not in data['entries']['0']['content']:
        data['entries']['0']['content'] += shiki_kenjutsu_mol

    # Entry 3: MEoDP
    shiki_meodp_mol = """

[NEURAL TRANSLATION: BYPASSING PHOTORECEPTOR TRANSDUCTION]
- Cortical Projection Without Retinal Intermediaries:
  * The visual manifestations of MEoDP—the intricate web of black lines and glowing points—are not formed by photons entering the cornea and focusing onto the fovea.
  * When Shiki closed her eyes, covered her face, or stayed in the pitch-black darkness of hospital room 404 in June 1998, the lines of death did not fade. The data is written directly onto her cerebral consciousness from Akasha, projecting structural mortality artifacts directly into her sensory cortex.
  * Zero-Enthalpy Conceptual Cleavage: Severing a line does not require kinetic work against intermolecular London dispersion forces or covalent bond enthalpy. The physical blade serves merely as a conceptual pointer; once the tip traverses the line's coordinate, the metaphysical existence of that connection is erased from Akasha, causing the physical matter to fall apart at the molecular boundary."""

    if "[NEURAL TRANSLATION: BYPASSING PHOTORECEPTOR TRANSDUCTION]" not in data['entries']['3']['content']:
        data['entries']['3']['content'] += shiki_meodp_mol

    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("01_Shiki.json updated successfully!")

def update_04_other_characters():
    fpath = 'Kara No/04_Other_Characters.json'
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Entry 0: Araya
    araya_mol = """

[CELLULAR IMMUNITY & ŚARĪRA DIAMOND OSSIFICATION]
- Transmutation of Biological Tissue:
  * Over four centuries of ascetic isolation, the three holy Śarīra relics embedded in Araya's left arm and thoracic cavity have replaced his organic skeletal matrix with a crystalline vajra-relic lattice.
  * Cellular Homeostasis: His somatic cells do not undergo mitotic senescence; DNA replication errors and oxidative stress from reactive oxygen species (ROS) are completely halted by the relic's conceptual sanctity. His biological age is permanently frozen.
  * Spatial Boundary Compression: Araya's personal Bounded Field contracts spatial volume, increasing the effective spatial metric between incoming blades and his body, draining projectile kinetic energy through metric expansion."""

    if "[CELLULAR IMMUNITY & ŚARĪRA DIAMOND OSSIFICATION]" not in data['entries']['0']['content']:
        data['entries']['0']['content'] += araya_mol

    # Entry 1: Fujino
    fujino_mol = """

[NOCICEPTIVE NEURO-PHARMACOLOGY & APPENDICEAL PATHOLOGY]
- Pharmacological Deactivation of Nociceptor Pathways:
  * Fujino's congenital analgesia (congenital insensitivity to physical pain) was not natural genetic insensitivity, but a chemically induced condition maintained from childhood by her family.
  * Spinal Depressant Action: Chronic administration of specialized spinal and nerve depressants inactivated the voltage-gated sodium channels (Na_v 1.7 and Na_v 1.8) along her primary afferent nociceptors—specifically the thinly myelinated A-delta fibers (transmitting acute, sharp pain) and unmyelinated C-fibers (transmitting chronic, burning visceral pain).
  * Consequently, action potentials failed to ascend through the dorsal root ganglion to the dorsal horn of the spinal cord, blocking transmission along the spinothalamic tract to the ventral posterolateral (VPL) nucleus of the thalamus and primary somatosensory cortex (S1). Fujino lived in a sensory void where cuts, burns, fractures, and sexual trauma produced zero conscious pain feedback.
- Transmural Appendiceal Gangrene & Neurochemical Storm:
  * In July 1998, acute appendicitis developed into transmural ischemic necrosis of the vermiform appendix wall. Bacterial overgrowth (Escherichia coli, Bacteroides fragilis) caused micro-perforation, releasing toxic purulent exudate into the peritoneal cavity (acute peritonitis).
  * The resulting inflammatory cascade released massive concentrations of inflammatory mediators: bradykinin, prostaglandin E2 (PGE2), serotonin, histamine, and substance P.
  * This colossal biochemical barrage generated continuous, high-amplitude depolarization of primary nociceptor nerve endings that completely overpowered and incinerated the pharmacological blockade in her spinal cord. Pain signals flooded her cerebral cortex in an agonizing deluge, and the sudden restoration of sensation triggered the violent, uncontrollable awakening of her Mystic Eyes of Distortion."""

    if "[NOCICEPTIVE NEURO-PHARMACOLOGY & APPENDICEAL PATHOLOGY]" not in data['entries']['1']['content']:
        data['entries']['1']['content'] += fujino_mol

    # Entry 4: Lio
    lio_mol = """

[CELLULAR, ODONTOLOGICAL & NEUROCHEMICAL PREDATORY MUTATION]
- Origin Awakening — Consumption (喰意, Shokui):
  * When Araya Souren forcefully unlocked Shirazumi Lio's Origin, the dormant genetic and metaphysical memory of primitive mammalian predation reasserted itself, triggering severe somatic and biochemical alterations.
- Odontological & Musculoskeletal Alterations:
  * Hypertrophy of Masticatory Muscles: The bilateral masseter, temporalis, and medial pterygoid muscles underwent rapid hypertrophy, elevating Lio's maximum bite force from the normal human baseline (~700 Newtons) to well over 2,200 Newtons, enabling him to crush human cranial bones and sever tendons with his teeth.
  * Tooth Enamel Micro-Hardness: His dental enamel underwent accelerated remineralization and micro-densification, anchoring deeply into reinforced alveolar bone sockets to withstand the extreme mechanical torque of tearing raw muscle and cartilage.
- Hyper-Sensitized Olfactory Epithelium:
  * Upregulation of olfactory receptor neurons in the nasal cribriform plate allowed Lio to detect airborne trace molecules down to parts-per-billion concentrations. He could chemically parse individual volatile compounds: oxidized iron from hemoglobin, lactic acid in human sweat, and elevated cortisol concentrations in the perspiration of terrified prey amidst miles of urban smog and rain.
- Neurochemical Endorphin Rush of Cannibalism:
  * Ingesting human flesh triggered massive, supra-physiological surges of dopamine in his nucleus accumbens and beta-endorphins throughout his central nervous system, producing an intoxicating, euphoric analgesia that silenced all moral inhibition and transformed cannibalism into an irresistible neurochemical addiction."""

    if "[CELLULAR, ODONTOLOGICAL & NEUROCHEMICAL PREDATORY MUTATION]" not in data['entries']['4']['content']:
        data['entries']['4']['content'] += lio_mol

    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("04_Other_Characters.json updated successfully!")

def update_03_touko():
    fpath = 'Kara No/03_Touko.json'
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Entry 3: Touko Magecraft & Puppetry
    touko_craft_mol = """

[MOLECULAR HOMOLOGY IN GRAND PUPPET CELLULAR ARCHITECTURE]
- Absolute Genetic & Cytological Parity:
  * Touko's synthetic puppet bodies achieve complete cellular homology with natural human tissue.
  * Ribosomal & Mitochondrial Synthesis: Synthetic cytoplasmic organelles perform normal metabolic respiration, producing adenosine triphosphate (ATP) via authentic oxidative phosphorylation.
  * Hematopoietic Bone Marrow: Active vascularized marrow cavities produce erythrocytes and leukocytes with exact antigen matching (ABO and Rh groups), ensuring that the puppet bleeds, clots, and scabs with biological realism indistinguishable from a living human body under microscopic biopsy.
  * Synthetic Magic Circuit Weave: Thaumaturgical circuit pathways are bio-chemically synthesized directly into peripheral nerve sheaths, matching the conduction velocity of natural human nerve impulses."""

    if "[MOLECULAR HOMOLOGY IN GRAND PUPPET CELLULAR ARCHITECTURE]" not in data['entries']['3']['content']:
        data['entries']['3']['content'] += touko_craft_mol

    # Entry 9: Touko Combat Arsenal & Familiar
    touko_arsenal_mol = """

[RUNE PLASMA KINETICS & GLOOM BEAST ETHER DENSITY]
- Ansuz Rune Thermal Plasma Ionization:
  * Carving the Ansuz (ᚫ) rune using prana-infused cigarette smoke or fingertips establishes an extreme localized thaumaturgical potential gradient.
  * Ambient diatomic nitrogen (N2) and oxygen (O2) molecules undergo rapid ionization, shedding valence electrons and forming a miniature non-equilibrium thermal plasma channel. The instantaneous exothermic energy release ignites cigarette tobacco leaf hydrocarbons in under 15 milliseconds without mechanical ignition aids.
- Briefcase Gloom Beast Molecular-Ether Duality:
  * Touko's sealed familiar—the ancient shadow entity stored within her vintage leather briefcase—operates on fluctuating phase density.
  * In storage or stalking mode, it exists as a coherent mass of dark ether lacking baryonic mass, slipping through air gaps and microscopic floor seams. Upon offensive deployment, it condenses its etheric density into an ultra-dense, semi-organic mass capable of exerting hundreds of atmospheres of compressive hydrostatic force, devouring victims (such as Cornelius Alba) down to molecular bone shards."""

    if "[RUNE PLASMA KINETICS & GLOOM BEAST ETHER DENSITY]" not in data['entries']['9']['content']:
        data['entries']['9']['content'] += touko_arsenal_mol

    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("03_Touko.json updated successfully!")

def update_16_everyday():
    fpath = 'Kara No/16_Everyday_Life_and_Personal_Details.json'
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Entry 0: Shiki Wardrobe & Domestic
    shiki_everyday_mol = """

[MICROSCOPIC TEXTILES & TACTILE THERMAL SENSITIVITY]
- Micro-Weave of Traditional Textiles:
  * Shiki's traditional kimono are woven from hand-spun Habutai silk and Echigo linen fibers, exhibiting microscopic surface friction that rustles softly against cotton inner nagajuban and leather ankle wraps.
  * The friction of leather boot lining against bare ankles creates subtle tactile sensory input that anchors her somatic awareness.
- Ice Cream Thermodynamic Phase Transition & TRPM8 Activation:
  * When consuming Häagen-Dazs strawberry ice cream in her unheated apartment, the frozen lipid-emulsion (butterfat crystals, sugar matrix, and frozen strawberry juice) undergoes an endothermic phase transition at oral temperature (37°C).
  * The sudden absorption of latent heat activates the lingual TRPM8 cold-receptor ion channels in her tongue and palate, sending sharp sensory impulses along the lingual nerve to the brain stem—a grounding tactile sensation that affirms her living physical reality."""

    if "[MICROSCOPIC TEXTILES & TACTILE THERMAL SENSITIVITY]" not in data['entries']['0']['content']:
        data['entries']['0']['content'] += shiki_everyday_mol

    # Entry 2: Touko Workshop & Vices
    touko_everyday_mol = """

[CHEMICAL PYROLYSIS & TOBACCO ALKALOID AEROSOLS]
- French Dark Tobacco Pyrolysis:
  * Touko's preferred Gitanes and Gauloises cigarettes consist of air-cured dark tobaccos. Pyrolysis produces dense aerosols rich in volatile alkaloids (nicotine, nornicotine) and heterocyclic pyrazines (2,3,5-trimethylpyrazine), imparting a pungent, dry, woody aroma.
  * These heavy aerosolized tars deposit microscopic residues onto the glass lenses of Touko's optical benches, antique mahogany tables, and wooden puppet joints across the Garan no Dou warehouse."""

    if "[CHEMICAL PYROLYSIS & TOBACCO ALKALOID AEROSOLS]" not in data['entries']['2']['content']:
        data['entries']['2']['content'] += touko_everyday_mol

    # Entry 6: Fujino Poise & Sensory Recovery
    fujino_everyday_mol = """

[MICRO-NOCICEPTION & CUTANEOUS SENSORY RE-INNERVATION]
- Cutaneous Sensory Reawakening:
  * Following the surgical appendectomy and the restoration of her nervous pathways, Fujino experiences the slow re-innervation of cutaneous mechanoreceptors (Meissner's corpuscles and Merkel nerve endings).
  * Cold rainwater drops falling onto her shoulders produce crisp, distinct tactile and thermal feedback, contrasting sharply with the dead numbness of her youth.
  * Deep within her lower right abdomen, the healing scar tissue over the appendectomy incision generates persistent, low-amplitude visceral throbs—a constant, grounding reminder that she is human and can feel pain."""

    if "[MICRO-NOCICEPTION & CUTANEOUS SENSORY RE-INNERVATION]" not in data['entries']['6']['content']:
        data['entries']['6']['content'] += fujino_everyday_mol

    # Entry 9: Lio Predator Reality
    lio_everyday_mol = """

[MICRO-OLFACTORY PARSING & CHEMICAL VOLATILITY]
- Airborne Volatile Organic Compound (VOC) Parsing:
  * Lio's hyper-developed olfactory epithelium allows him to dissect complex urban air masses. Amidst the diesel soot, industrial sulfur dioxide, and wet asphalt ozone of rainy Mifune City, he can isolate the distinct volatile chemical signature of oxidized iron from human blood (ferritin/porphyrin complexes) down to sub-nanomolar concentrations."""

    if "[MICRO-OLFACTORY PARSING & CHEMICAL VOLATILITY]" not in data['entries']['9']['content']:
        data['entries']['9']['content'] += lio_everyday_mol

    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("16_Everyday_Life_and_Personal_Details.json updated successfully!")

if __name__ == '__main__':
    update_06_abilities()
    update_01_shiki()
    update_04_other_characters()
    update_03_touko()
    update_16_everyday()
    print("All molecular expansions applied successfully!")

