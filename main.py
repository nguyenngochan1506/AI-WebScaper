import streamlit as st
from scrape import (scrape_website, split_dom_content, clean_body_content, extract_body_content,)
from parse import parse_with_ollama

st.title("AI Web Scraper")
url = st.text_input("Nhập vào đường dẫn của trang web: ")

if st.button("Thu Thập Dữ Liệu"):
    st.write("Đang thu thập dữ liệu...")
    
    result = scrape_website(url)
    st.write("Thu thập dữ liệu thành công!")
    
    body_content = extract_body_content(result)
    cleanned_content = clean_body_content(body_content)
    
    st.session_state.dom_content = cleanned_content
    
    with st.expander("Xem Nội Dung Được Thu Thập"):
        st.text_area("DOM Content: ", cleanned_content, height=300)
    

if "dom_content" in st.session_state:
    parse_description = st.text_area("Bạn muốn làm gì vơi dữ liệu này?")
    
    if st.button("Xử Lý Dữ Liệu"):
        if parse_description: 
            st.write("Đang tiến hành xử lý dữ liệu...")
            
            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks, parse_description)  
            print("Xử lý hoàn tất!") 
            st.write(result)