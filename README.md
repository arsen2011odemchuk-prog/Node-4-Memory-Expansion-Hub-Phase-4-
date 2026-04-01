# Hydra Node 4: Memory Expansion Unit

Node 4 is designed to provide **additional storage** for the Hydra Cluster without requiring a full PC build. Its primary function is to host **1–2 NVMe SSDs** and allow easy access for the main compute nodes. Node 4 is mounted above Node 3 in an **open-air setup**, supported by fiberglass tubes and a single mounting plate.

## 🧠 Purpose
Node 4 serves as a **dedicated storage node**, expanding cluster memory while keeping power and heat minimal. It relies on Node 1 for overall compute control and does not require a high-performance CPU.

## 🛠️ Hardware Specifications
- **Motherboard:** Mini-ITX or Micro-ATX with DDR4 support and at least 1 NVMe slot (Gigabyte a520i ac, ASRock A520M-ITX/ac, or similar)  
- **CPU:** Budget Celeron or AMD Athlon (used or new low-power)  
- **RAM:** 8 GB DDR4 SO-DIMM (for basic operation)  
- **Storage:** 1 TB NVMe SSD (primary), optional second SSD via PCIe adapter or USB-to-NVMe  
- **Cooling:** 2× 120 mm fans powered from Node 1 PSU  
- **Support Structure:** Fiberglass tubes + single mounting plate  
- **Power Regulation:** 12 V → 5 V step-down converter for motherboard
  <img width="832" height="595" alt="Знімок екрана 2026-04-01 о 03 37 23" src="https://github.com/user-attachments/assets/7e6cd756-be9b-46b6-95e0-5e0677be166c" />
<img width="603" height="446" alt="image" src="https://github.com/user-attachments/assets/85b01a6b-04cf-486a-9bc9-50887d63ffaa" />
<img width="617" height="516" alt="image" src="https://github.com/user-attachments/assets/0687a5da-d7e9-45a9-a806-84a716747146" />


## 🔌 Connections & Wiring
- **Power:** Node 4 receives 12 V from Node 1 PSU, stepped down to 5 V for the motherboard and SSDs. Fans powered via Node 1 12 V line.  
- **Storage:** Primary NVMe SSD plugs directly into motherboard M.2 slot. Second SSD plugs into PCIe NVMe adapter or USB adapter if motherboard lacks extra slots.  
- **Communication:** Node 4 storage is accessed by Node 1 via internal network or USB sharing. Node 4 does not perform heavy computation.  

## 📦 Bill of Materials (BOM)

| Component | Model/Type | Est. Price £/$ |Link|
|-----------|------------|----------------|----|
| Motherboard |Micro-ATX| £46.99 / $61,94 |[amazon](https://www.amazon.co.uk/Gigabyte-Motherboard-Bandwidth-Management-Anti-Sulfur/dp/B0BXFBN121/ref=sr_1_3?crid=1CKDOWR1EA9C8&dib=eyJ2IjoiMSJ9.0-NWM1H04av2We_l2x1LOysRaMFT_z_S_zTYr0qAzv0Wmjo0u4c8gelcowUN9RSNHpGlzDoO556Y1XxPbj4bESKKDJaWhCfojarNvWOYsG76mHZwGNS4pRPPGOpgMdsRWFsZLFRqiJzPuJ_kk_2U9YaUlQ-UYOc91tvN0Tey2JzQTN6uY7k88vijscSvx8H5h_XmOZ-goOzv-ovn3mibWbNA9hJnIh5STdiC3LxfJQ8XfmwIBSqtEDn8bBXZWtvR3KtqpNFnUZxC1vOwH_toPNVFgs1mSAQ1BG3typJc-u4.HVXP9LihjgPbIkHzLtgzwptoe5CknEumzD2mn1UlPu8&dib_tag=se&keywords=Micro-ATX&qid=1775008243&s=computers&sprefix=micro-atx%2Ccomputers%2C262&sr=1-3&th=1)|
| CPU | Celeron / AMD Athlon (budget) | £48.85  / $64,39 |[amazon](https://www.amazon.co.uk/AMD-Ryzen-4100-processor-8-thread/dp/B09VCRQVWM/ref=sr_1_2?crid=3BNEA4ZGM9OF0&dib=eyJ2IjoiMSJ9.n4fb5L63hGFpNegqWHJ2dEve7yzXK2mO5qV6_x6RPnzrxdzHe_vn_uix4sp8ibOIbczOrHXXgXqa4PRoTG_F18RYqaK-XQy89fj9lY-AIXh2u_gyl_HW32B6TDEHpjKrj0Fl4blcr23HN2I9MWqiPW8aC0WnkyAqg79lO3eNbiGBBjLa4IPSqp9Zjeo3BWPuTXTPehsoZXn2RsW0vhp7aKE0ywau4n_IJ4xRUpFIDma2ofvySEX23M95AMtMlzc6oDV7BjJ5Ce06QvP7hhbaHNX9m4tN3gIyiN0zEH6kvZ4.P3AjLFbNZdrIzeZzhduVjng73_V-7-lb2fnKNKwo6Uo&dib_tag=se&keywords=AMD%2BAthlon&qid=1775008313&s=computers&sprefix=%2Ccomputers%2C277&sr=1-2&th=1)|
| RAM | 4 GB DDR4 SO-DIMM | £18.99 / $25,03 |[amazon](https://www.amazon.co.uk/JAZER-DDR4-2400MHZ-288-PIN-Heatsink-Red/dp/B09QS6TFN5/ref=sr_1_9?crid=O8GYPIDVOBR1&dib=eyJ2IjoiMSJ9.Th8749ydQhmuMuC7MdsqsKzyj0ByzsZbV_27vdw4QZLzsaKcql-RpXfVlIfGUKGJCRQ3z_weoJoi4WcAqlodcZRiaINGF8hTkQ9QLo2Hds2GgEBu0uMDSTTXYu-DapaC_q6ejtu0G25L7eTh_XOMUKCTOydWTud1LMl69NE4fam01rHWeMKZurroCX_pyE_eTtvy0pzxp2MMdP0Xal59eQd-AMIImbgZ08h6B-LRnq0.4IFBaayRhLPabzIOdxHdmEEQF7-sULIi7Sot5uNzQpQ&dib_tag=se&keywords=8GB+DDR4+%28Crucia&qid=1775010006&refinements=p_36%3A-2200&rnid=428432031&sprefix=8gb+ddr4+crucia%2Caps%2C297&sr=8-9)|
| SSD Storage | 1 TB NVMe SSD | £34.99 / $46,12 |[amazon](https://www.amazon.co.uk/Wadakada-1080PRO-Solid-State-7000MB/dp/B0F1FDST89/ref=sr_1_2?crid=3QQH9YXAX2P6I&dib=eyJ2IjoiMSJ9.BEnrP05ArpDsNrL_ktzsse0BxSckfT-3c1yWaEx0P1YFbqoTVakrcDUiswNVGMsS_3LtIlH1GX4IxelJAhMS8HfklHJlEQImpjh_9Nn_Kc4.FMHSq5xaUX43AIG1hdQKd35AE3CHY55CpjOcvA9GpAM&dib_tag=se&keywords=1%E2%80%AFTB+NVMe+SSD&qid=1775008489&refinements=p_36%3A-4000&rnid=428432031&s=computers&sprefix=%2Ccomputers%2C276&sr=1-2)|
| Second SSD (optional) | NVMe or SATA SSD | £34.99 / $46,12 |[amazon](https://www.amazon.co.uk/Wadakada-1080PRO-Solid-State-7000MB/dp/B0F1FDST89/ref=sr_1_2?crid=3QQH9YXAX2P6I&dib=eyJ2IjoiMSJ9.BEnrP05ArpDsNrL_ktzsse0BxSckfT-3c1yWaEx0P1YFbqoTVakrcDUiswNVGMsS_3LtIlH1GX4IxelJAhMS8HfklHJlEQImpjh_9Nn_Kc4.FMHSq5xaUX43AIG1hdQKd35AE3CHY55CpjOcvA9GpAM&dib_tag=se&keywords=1%E2%80%AFTB+NVMe+SSD&qid=1775008489&refinements=p_36%3A-4000&rnid=428432031&s=computers&sprefix=%2Ccomputers%2C276&sr=1-2)|
| PCIe NVMe Adapter | x4 NVMe to PCIe | £8.99 / $11,85 |[amazon](https://www.amazon.co.uk/Maxhood-Aluminum-Heatsink-Solution-Expansion/dp/B0F4X7FC65/ref=sr_1_11?crid=1YS7M07BGZIQL&dib=eyJ2IjoiMSJ9.HK7We7MJlxb6vZM8oVLkjAQAOHIAilEr28XWypP1wa15fHS6yYEfBA2BiE_bBe7AdcgD2CEmEWiJJKxVvOjZrwl8K8zSMvC2BYZVtFucBT6_xcvnVtixGujqc_uXJlGDf96mpFlW0R9Sq4bMQEZ5tCSQLF9fUeT1Qk6j4ShLrKfQXGA1tMiVhWEczC7n2TcVsZXz-26fuIfJ_3lJ-vVo9XICDb5bhpG-dHDeF9thE4c8ojSXmc7dVVQ7ij3HPvpmGq7UjhdcddxKf8LARIrrPyIN_Rxtr0Ack8tS2mt4cl4.J4-oS--y0th15feE-WEDS9eWhLgEnHdZBqGdFRoj07M&dib_tag=se&keywords=x4%2BNVMe%2Bto%2BPCIe&qid=1775008535&s=computers&sprefix=x4%2Bnvme%2Bto%2Bpcie%2Ccomputers%2C322&sr=1-11&th=1)
| Fiberglass Wire | Inforamation trasfer | £7.21/$ 9.50|[amazon](https://www.amazon.co.uk/Ethernet-Telephone-Broadband-Extension-Compatible-White/dp/B07XQ4GZ84/ref=sr_1_12?crid=1Q1J7Z5A4KO8Z&dib=eyJ2IjoiMSJ9.jhaj8gNrYHoLlYi7Ye1k5kHnTU4KeQXsaWDd_7UEsExxNol60fKSjYL1ajVBnB2r1Acb118GM5PZTe90CTOpIv0QtblU0pLU6vNigi_1TwBhK038gVbT3sw4nLfunnFJPJKjsVKD690cedNfyFDZoXkgUDGKydgSmvg5yCtbXDSrd_umR3VtufbM2kLY165qdsHvjZrN3m0mgWw1DYtAhb7jfGRGxQfsliY2UTzjA7wmi1nUGYyFIJ0R136N6fJtiF1JlChT7j7NOvFKrK-G3WmHlglMQz1-UB2TC-DiVQg.Bo1hd25Q3iYlQBBIRXxWoSd1qh3SDi4mVY7EPjWJiTw&dib_tag=se&keywords=Fiberglass%2Bwires%2Bwith%2Badapter%2Bfor%2Binternet&qid=1775008907&s=industrial&sprefix=fiberglass%2Bwires%2Bwith%2Badapter%2Bfor%2Binterne%2Cindustrial%2C330&sr=1-12&th=1)|
| 260 Pcs M3 Male Female Nylon Hex Spacer Standoffs Screws Nuts, Nylon Hex Threaded Pillar  | Mounting | £6.99 / $9,21 |[amazon](https://www.amazon.co.uk/Standoffs-Threaded-Assortment-Circuit-Motherboard/dp/B09C21MS45/ref=sr_1_1_sspa?crid=3FEVWM6U30SNW&dib=eyJ2IjoiMSJ9.CVrDpsyW7JZkWN4o5qAFkkHv8I8CxJUg_lN3-OMoi_ZApuYT2tsxGnnAkiZ5TxXR4cR46oi68Hd6i4LZ1WRrDGfPXK_hGfJLJ0jcn4SZnJSsWF9TlHO5ElC4v22XfEQ57Em1OSeGOYtXMcbRvBHM1IrfXKgchBAElOzQytYteLcEEnE4fP9tTpW8TGbvqSKcRzN98pe5aauNdSI6-ltkV2gbgRE3NA_LkbLjXZeOCxdoWuBE5ndUovTonWoWxIunMaqpuczfeLADzoaLYsvd3jxP9hcdCuM7b-dvoTrnmzI.R6bZot4BJ4MyKY_0WSoe2nIQmXm3zsl6F6s97DDz-l4&dib_tag=se&keywords=M3%2BScrews%2B%26%2BStandoffs&qid=1775009016&refinements=p_36%3A-700&rnid=118657031&s=industrial&sprefix=%2Cindustrial%2C272&sr=1-1-spons&aref=a4B5lZ4Hih&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1)|
| Cable Ties / Clips | Wire management | £5.94 /$7,83 | [amazon](https://www.amazon.co.uk/JatilEr-Adhesive-Holders-Multi-Purpose-Pads-Black/dp/B08ML9FTNB/ref=sr_1_1_sspa?dib=eyJ2IjoiMSJ9.Iekbml361DzKgrzk-PebsMr5LmJRoYmiIll5pgIoS1y_jSZpm02t69cz6Ud-taFW_6h2xCJX0iHZnxEKJccW6AaR3WsZaETJLmlApi5NUP1gNLIbvzpbU1D8MMwaH8lvfK9ohgeyprdxSS8GYUTjcmm0UtHXmfVZ8tDF0C19jW2SUzjPTjiw3ImaogUjqX6Ktvo7rnLD-B1WFMwg39Dt5go1Q1Dqh4_EWRftiTZWspsKMa_E_WiDEXMVkiCbbv21nmh-UBrjjuSc1HlGuH0y_iTplrmpV60jshw14UPmyCM.aXXeu7bGM74Q1a4pYVGTfNKSxZcameed_ZAXy2974qs&dib_tag=se&keywords=Cable+Ties+%2F+Clips&qid=1775009052&sr=8-1-spons&aref=jK4uLujUNE&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1) |
| Open-Air Case | For stacking Node 4 above Node 3 | £24.66 / $32.51 |[Amazon](https://www.amazon.co.uk/Bench-Frame-Computer-Chassis-Techbench-Black/dp/B0FPFXVQ1H/ref=sr_1_13?crid=26FKH9U0FYOHX&dib=eyJ2IjoiMSJ9.5MCzBAV1Y22LlUcolgJ0l0kIIp_lBfwsqSxg4jQwFKzdqQWlfKT4u_Iu67fRKem-fFXTkDvb9KcyQZ7R5OhkP2TAJBgLoaMqLD4TvJpULWfWOWS0dauQ5mOlpqEsrSsmkqE84s8rn-zyWa5-PooDUO3oa00unzFoLisdgpSVEDAOgicGHWf8HMjRomP6i-qfzXiE07mloPKB9wyZO9j_WAPm_d_5XAhQy5vGD2EIqPI.mnR93i8T_A9Hqr9a90NcnL-h8BjbPC1vStNizkkdm1w&dib_tag=se&keywords=Open-Air+Case&qid=1775009260&sprefix=open-air+case+%2Caps%2C267&sr=8-13)
| **PSU** | Power Node 4 |£60.05/$79,16 |[amazon](https://www.amazon.co.uk/CORSAIR-Bronze-Modular-Low-Noise-Supply/dp/B0CJRXNXZT/ref=sr_1_1?crid=33VZHC4RI5SMD&dib=eyJ2IjoiMSJ9.lcg6jozQpt-oJbHGu26C0dhqWAcflNtXbdHMX29eW9s-hehXB_DDbQg9qEnc0xOhO2bmdf_D7CEsXggyK-rFlglGW67976ef3SIkycsBoIVOSJi-ri041IKQKJzn72zjZzgag13j0d8Q_Rl34_JQ0A.U4aXddOQkidAlrPKo4TVtbOZD39hwu3Ht75vEwvWlLk&dib_tag=se&keywords=Corsair%2BRM650e&qid=1775010168&refinements=p_36%3A-6400&rnid=405443031&sprefix=corsair%2Brm650e%2Caps%2C288&sr=8-1&th=1)|
**Estimated Total:** £298.65 / $ 393,67 

## 📝 Notes
- Node 4 is primarily a storage node and relies on Node 1 for heavy compute.  
- Fiberglass tubes provide lightweight, strong support above Node 3.  
- Cooling is minimal since no high-power CPU is used; 2× 120 mm fans maintain airflow.  
- Step-down converter ensures safe, continuous 24/7 operation from Node 1 PSU.  
