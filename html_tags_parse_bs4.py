from bs4 import BeautifulSoup
tag = '''<div class="supplementation-report">
 <section class="page">
  <strong>
   Fotografování tříd proběhne v úterý 19. dubna 2022 podle níže uvedeného rozpisu:
  </strong>
  <ul>
   <li>
    -1.A    8:00           2.A    8:30           3.A    10:10         4.A    10:30
   </li>
   <li>
    -1.B    8:10           2.B    8:40           3.B    8:50           4.B    12:30
   </li>
   <li>
    -1.C    11:00         2.C    10:00         3.C    9:30           4.C    12:35
   </li>
   <li>
    -1.G    8:20           2.K    9:00           3.K    9:20           4.K    10:40
   </li>
   <li>
    -1.K    11:10         2.L    9:10           3.L    10:20         4.L    10:50
   </li>
   <li>
    <hr/>
   </li>
  </ul>
  <strong>
   Suplování na úterý 19. 4. 2022
  </strong>
  <ul>
   <li>
    -1.A 2.h. MAT Rk - odborně zastupuje Zk ve 206 – přijde celá třída
   </li>
   <li>
    -1.A 4.h. FYZ Rk - odborně zastupuje Kj ve 206 – přijde celá třída
   </li>
   <li>
    -1.B 1.h. FYZ Rk - odborně zastupuje Zk ve 113 – přijde celá třída
   </li>
   <li>
    -1.C 3.h. FYZ Rk - odborně zastupuje Kj ve 318 – přijde celá třída
   </li>
  </ul>
  <hr/>
 </section>
</div>'''

meta = BeautifulSoup(tag, 'html.parser')
soup = meta.find("section", attrs={"class":"page"})

for data in soup.find_all('strong'):
    title = data.get_text()
    print('TITLE :',title)
    for inner_data in soup.find_all('li'):
        if inner_data:
            print(inner_data.get_text())
    print("*"*70)
