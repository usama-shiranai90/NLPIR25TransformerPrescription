from scholarly import scholarly
import csv
import time
import random
import argparse

def scrape_scholar(query, limit=None, output_file="google_scholar_works.csv"):
    print(f"Searching for: {query}")
    search_query = scholarly.search_pubs(query)
    
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        headers = ['title', 'author', 'pub_year', 'venue', 'abstract', 'pub_url', 'num_citations', 'cites_id']
        writer.writerow(headers)
        
        count = 0
        try:
            for result in search_query:
                if limit and count >= limit:
                    break
                
                bib = result.get('bib', {})
                title = bib.get('title', '')
                author = bib.get('author', [])
                if isinstance(author, list):
                    author = '; '.join(author)
                pub_year = bib.get('pub_year', '')
                venue = bib.get('venue', '')
                abstract = bib.get('abstract', '')
                pub_url = result.get('pub_url', '')
                num_citations = result.get('num_citations', 0)
                cites_id = result.get('cites_id', '') 
                
                writer.writerow([title, author, pub_year, venue, abstract, pub_url, num_citations, cites_id])
                count += 1
                print(f"Saved {count}: {title[:50]}...")
                
                # Sleep to avoid rate limiting
                time.sleep(random.uniform(1, 3))
                
        except StopIteration:
            print("No more results found.")
        except Exception as e:
            print(f"An error occurred: {e}")
            
    print(f"Finished. Saved {count} records to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape Google Scholar")
    parser.add_argument("--limit", type=int, default=None, help="Limit the number of results")
    args = parser.parse_args()
    
    query = """(transformer* OR "self-attention" OR BERT OR GPT OR "large language model" OR "retrieval-augmented generation") AND (prescrib* OR medicat* OR "drug" OR pharmac* OR "medication recommendation" OR prescription)"""
    
    scrape_scholar(query, limit=args.limit)
