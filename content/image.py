array = ['image/gallery/8B2EBBE2-7375-4A58-ADFB-0558AC018D98-1408-000003BEAAB3D115_tmp.jpg',
'image/gallery/651B194B-C72D-4D75-A3F8-913803A534FC-379-000001BC6FDE368B_tmp.jpg',
'image/gallery/cykel-1.JPG',
'image/gallery/dricka.JPG',
'image/gallery/IM-2016-1.jpg',
'image/gallery/IM-2022-1.JPG',
'image/gallery/IM-2022-2.JPG',
'image/gallery/IM-2022-3.JPG',
'image/gallery/IM-2022-4.jpg',
'image/gallery/IMG_3473.JPG',
'image/gallery/KarlstadTrOlympicLogo-0000138.jpg',
'image/gallery/KarlstadTrOlympicLogo-0000242.jpg',
'image/gallery/mal_pust.JPG']

myString = ""

for i in array:
    myString += (f"""<a href="{i}" target="_blank"><picture class="gallery-item">
<source media="(min-width: 768px)" srcset="{i}?h=160&w=240&crop-to-fit&save-as=jpg">
<source media="(max-width: 767px)" srcset="{i}?w=720&save-as=jpg">
<img src="{i}?w=720&save-as=jpg" alt="Image description">
</picture></a>""")
    
with open('resultat.txt', 'w') as f:
    f.write(myString)

