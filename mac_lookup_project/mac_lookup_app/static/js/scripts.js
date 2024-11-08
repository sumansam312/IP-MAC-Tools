document.getElementById("abbrForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const abbreviation = document
    .getElementById("abbreviation")
    .value.trim()
    .toUpperCase();

  const abbreviationDetails = {
    SOC: {
      fullForm: "Security Operations Center",
      description:
        "A facility for monitoring and responding to security incidents in real-time.",
    },
    DFIR: {
      fullForm: "Digital Forensics and Incident Response",
      description:
        "A field of study and practice focused on investigating cyber incidents and recovering evidence.",
    },
    SIEM: {
      fullForm: "Security Information and Event Management",
      description:
        "A set of tools for detecting, monitoring, and responding to security events and incidents.",
    },
    OSSTMM: {
      fullForm: "The Open Source Security Testing Methodology Manual",
      description:
        "A comprehensive security testing methodology for organizations to assess security.",
    },
    OWASP: {
      fullForm: "Open Web Application Security Project",
      description:
        "An online community working to improve the security of software through open-source resources.",
    },
    NIST: {
      fullForm: "National Institute of Standards and Technology",
      description:
        "A U.S. government agency responsible for setting cybersecurity standards, guidelines, and practices.",
      link: "https://www.nist.gov/cyberframework",
    },
    NCSC: {
      fullForm: "National Cyber Security Center",
      description:
        "A UK government agency that provides support and guidance on cybersecurity issues.",
    },
  };

  // Check if abbreviation exists in our details
  const details = abbreviationDetails[abbreviation];

  if (details) {
    displayResults(
      abbreviation,
      details.fullForm,
      details.description,
      details.link
    );
  } else {
    alert("Abbreviation not found. Please try again.");
    document.getElementById("resultsContainer").style.display = "none";
  }
});

function displayResults(abbreviation, fullForm, description, link = "") {
  const resultsBody = document.getElementById("resultsBody");
  resultsBody.innerHTML = `
    <tr>
      <td>${abbreviation}</td>
      <td>${fullForm}</td>
      <td>${description} ${
    link ? `<a href="${link}" target="_blank">More Info</a>` : ""
  }</td>
    </tr>
  `;
  document.getElementById("resultsContainer").style.display = "block";
}
